from fastapi import FastAPI
from src.routes.users import user

app = FastAPI(
    title='FastAPI SQLAlchemy CRUD',
    description='FastAPI SQLAlchemy CRUD with MySQL',
    version='0.0.1',
    openapi_tags=[
        {
            'name': 'users',
            'description': 'Users CRUD operations'
        }
    ]
)


app.include_router(prefix='/users', router=user)
