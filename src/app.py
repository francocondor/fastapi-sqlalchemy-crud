from fastapi import FastAPI
from src.routes.users import user

app = FastAPI()

app.include_router(prefix='/users', router=user)