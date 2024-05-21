from http.client import HTTPException

from pydantic import BaseModel, constr, ValidationError


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    email: constr(pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    password: str

