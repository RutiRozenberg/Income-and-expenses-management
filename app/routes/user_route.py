from fastapi import APIRouter, HTTPException

from app.models.User import User
from app.services.user_service import signIn_service, signUp_service

user_router = APIRouter()


@user_router.get("/signIn/{email}/{password}")
async def signIn(email, password):
    user = await signIn_service(email, password)
    if not user:
        raise HTTPException(status_code=404, detail="oops... user didn't find")
    return user


@user_router.post("/signUp")
async def signUp(user: User):
    if not await signUp_service(user):
        raise HTTPException(status_code=400, detail="oops... invalid parameters")
    return True
