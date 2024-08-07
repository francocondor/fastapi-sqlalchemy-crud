from fastapi import APIRouter
from config.db import conn
from models.users import users

user = APIRouter()


@user.get('/')
async def get_users():
    return conn.execute(users.select()).fetchall()


@user.get('/{user_id}')
async def read_user(user_id: int):
    return {'msg': f'Read User {user_id}'}


@user.post('/')
async def create_user():
    return {'msg': 'Create User'}


@user.put('/{user_id}')
async def update_user(user_id: int):
    return {'msg': f'Update User {user_id}'}


@user.delete('/{user_id}')
async def delete_user(user_id: int):
    return {'msg': f'Delete User {user_id}'}
