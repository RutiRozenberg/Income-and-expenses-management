from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signin_valid_credentials():
    response = client.get("/user/r@gmail.com/rr")
    assert response.status_code == 200  
    assert response.json() is not None  


def test_signin_not_found():
    response = client.get("/user/Not_found@example.com/Not_found")
    assert response.status_code == 404  
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_invalid_credentials():
    response = client.get("/user/rr/rer")
    assert response.status_code == 404
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_changing_parameters():
    response = client.get("/user/rr/r@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_without_password():
    response = client.get("/user/r@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_signin_without_parameters():
    response = client.get("/user")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

