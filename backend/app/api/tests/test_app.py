from fastapi.testclient import TestClient
from app import app  # تأكد من استيراد التطبيق الرئيسي

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
