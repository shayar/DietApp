from fastapi import FastAPI
from app.api import ai
from app.utils.logger import setup_logger

setup_logger()
app = FastAPI(
    title="AI Service",
    description="Demo FastAPI for AI endpoint",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "AI Service running"}

app.include_router(ai.router, prefix="/ai")
