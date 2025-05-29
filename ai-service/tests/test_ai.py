from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/ai/predict", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json()["result"] == "olleh"
