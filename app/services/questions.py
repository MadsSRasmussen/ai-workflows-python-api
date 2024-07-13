from app.schemas.questions import QuestionGenerate
from app.utils.questions import parse_variable_definition, random_variable_value, replace_question_variables

def generate_variations_from_data(question_data: QuestionGenerate):
    
    parsed_variables = [parse_variable_definition(variable) for variable in question_data.variables]
    variables = [[random_variable_value(variable) for variable in parsed_variables] for i in range(0, question_data.variations) ]

    return [replace_question_variables(question_data, variable) for variable in variables]