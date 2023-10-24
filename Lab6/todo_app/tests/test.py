import pytest
from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello!"}

def test_get_greeting_with_path():
    response = client.get("/greeting/John/Engineering")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, my name is John and I major in Engineering"}

def test_get_greeting_with_query():
    response = client.get("/greeting/?name=John&age=30")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello, I am John, who is 30 years old."}


def test_create_user():
    new_user_data = {
        "username": "test_user",
        "email": "test@example.com"
    }
    response = client.post("/create_user", json=new_user_data)
    assert response.status_code == 200
    assert response.json() == {"msg": "This is a POST API.", "new_user": new_user_data}



if __name__ == "__main__":
    pytest.main(["-v", "test.py", "--cov=main"])
