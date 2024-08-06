from fastapi import APIRouter

user = APIRouter()

@user.get('/')
async def read_users():
    return {'msg': 'Read Users'}

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
