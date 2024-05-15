from http.client import HTTPException

from pydantic import BaseModel, constr, ValidationError


class User(BaseModel):
    name: constr(pattern=r"^[a-zA-Z_]+$")
    email: constr(pattern=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    password: constr(pattern="^[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*$")

