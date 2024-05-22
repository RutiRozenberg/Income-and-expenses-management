from pydantic import BaseModel, field_validator

from app.validators.string_validator import validate_date_format


class Expenses(BaseModel):
    id: int
    user_email: str
    amount: int
    description: str
    target: str
    date: str

    @field_validator('date')
    def date_format(cls, date):
        validate_date_format(cls, date)

