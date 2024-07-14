import re
import random
import numpy as np
from typing import List
from app.schemas.questions import VariableDefinition, VariableValue, QuestionGenerate, Question

def parse_variable_definition(definition: str) -> VariableDefinition:
    
    pattern = r'@(\w+)\[(\d+(\.\d+)?):(\d+(\.\d+)?):(\d+(\.\d+)?)\]'
    match = re.match(pattern, definition)
    
    if not match:
        raise ValueError("Invalid variable definition format")
    
    symbol = match.group(1)
    min_value = float(match.group(2)) if '.' in match.group(2) else int(match.group(2))
    step_value = float(match.group(4)) if '.' in match.group(4) else int(match.group(4))
    max_value = float(match.group(6)) if '.' in match.group(6) else int(match.group(6))
    
    return VariableDefinition(min=min_value, max=max_value, step=step_value, symbol=symbol)

def random_variable_value(definition: VariableDefinition) -> VariableValue:

    num_steps = int((definition.max - definition.min) / definition.step)
    random_step = random.randint(0, num_steps)
    variable_value = definition.min + random_step * definition.step

    return VariableValue(symbol=definition.symbol, value=variable_value)

def replace_variables(input: str, variables: List[VariableValue]) -> str:
    
    resulting_str = input

    for variable in variables:
        resulting_str = resulting_str.replace("@" + variable.symbol, str(variable.value))
    
    eval_splits = resulting_str.split('§')
    for i in range(len(eval_splits)):
        if i % 2 != 0:
            eval_splits[i] = str(eval(eval_splits[i]))

    return ''.join(eval_splits)

def replace_question_variables(question: QuestionGenerate, variables: List[VariableValue]) -> Question:

    old_keys = [field[0] for field in question]
    resulting_question = {}
    question_dict = question.model_dump(exclude={'variables', 'variations'})
    keys = question_dict.keys()
    
    for key in keys:
        field_to_replace = question_dict[key]
        if isinstance(field_to_replace, list):
            resulting_question[key] = [replace_variables(field, variables) for field in field_to_replace]
        else:
            resulting_question[key] = replace_variables(field_to_replace, variables)
        
    return resulting_question