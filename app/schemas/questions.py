from pydantic import BaseModel
from typing import List, Union

class RadioButton(BaseModel):
    problem_text: str
    hint: str
    solution: str
    correct_answer: str
    wrong_answers: List[str]

class DropDown(BaseModel):
    problem_text: str
    hint: str
    solution: str
    correct_answers: List[str]
    wrong_answers: List[str]

Question = Union[RadioButton, DropDown]

class RadioButtonGenerate(BaseModel):
    problem_text: str
    hint: str
    solution: str
    correct_answer: str
    wrong_answers: List[str]
    variables: List[str]
    variations: int

class DropDownGenerate(BaseModel):
    problem_text: str
    hint: str
    solution: str
    correct_answers: List[str]
    wrong_answers: List[str]
    variables: List[str]
    variations: int

QuestionGenerate = Union[RadioButtonGenerate, DropDownGenerate]

class VariableDefinition(BaseModel):
    min: Union[int, float]
    max: Union[int, float]
    step: Union[int, float]
    symbol: str

class VariableValue(BaseModel):
    symbol: str
    value: Union[int, float]