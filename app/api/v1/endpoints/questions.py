from fastapi import APIRouter

from app.schemas.questions import QuestionGenerate
from app.services.questions import generate_variations_from_data

router = APIRouter()

@router.post("/")
def generate_variations(question: QuestionGenerate):
    return generate_variations_from_data(question)