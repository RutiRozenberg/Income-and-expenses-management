from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signin_valid_credentials():
    """
    Test sign-in with valid credentials.
    Expected result: 200 status code and non-null JSON response.
    """
    response = client.get("/user/r@gmail.com/rr")
    assert response.status_code == 200
    assert response.json() is not None


def test_signin_not_found():
    """
    Test sign-in for a user not found.
    Expected result: 404 status code and response detail "oops... user didn't find".
    """
    response = client.get("/user/Not_found@example.com/Not_found")
    assert response.status_code == 404
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_invalid_credentials():
    """
    Test sign-in with invalid credentials.
    Expected result: 404 status code and response detail "oops... user didn't find".
    """
    response = client.get("/user/rr/rer")
    assert response.status_code == 404
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_changing_parameters():
    """
    Test sign-in with changed parameters.
    Expected result: 404 status code and response detail "oops... user didn't find".
    """
    response = client.get("/user/rr/r@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "oops... user didn't find"}


def test_signin_without_password():
    """
    Test sign-in without providing a password.
    Expected result: 404 status code and response detail "Not Found".
    """
    response = client.get("/user/r@gmail.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_signin_without_parameters():
    """
    Test sign-in without providing any parameters.
    Expected result: 404 status code and response detail "Not Found".
    """
    response = client.get("/user")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
