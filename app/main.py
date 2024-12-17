from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routes.expense_route import expense_router
from app.routes.income_route import income_router
from app.routes.user_route import user_router
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])
app.include_router(user_router, prefix='/user')
app.include_router(income_router, prefix='/income')
app.include_router(expense_router, prefix='/expense')


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
