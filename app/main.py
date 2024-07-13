from fastapi import FastAPI

from app.api.v1.endpoints import questions
from app.core.logger import logger

app = FastAPI()

app.include_router(questions.router, prefix="/api/v1/questions", tags=["questions"])

@app.get("/")
def server_check():
    return "Server is running..."