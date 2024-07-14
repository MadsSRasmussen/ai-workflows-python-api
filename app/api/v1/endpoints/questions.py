from fastapi import APIRouter, HTTPException

from app.schemas.questions import QuestionGenerate
from app.services.questions import generate_variations_from_data

router = APIRouter()

@router.post("")
def generate_variations(question: QuestionGenerate):
    try:
        return generate_variations_from_data(question)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unable to generate variables")