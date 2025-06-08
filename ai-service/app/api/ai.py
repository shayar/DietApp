from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PredictRequest(BaseModel):
    text: str

@router.post("/predict", summary="Reverse text", response_description="The reversed string")
def predict(req: PredictRequest):
    """A demo AI endpoint that reverses input text."""
    return {"result": req.text[::-1]}

