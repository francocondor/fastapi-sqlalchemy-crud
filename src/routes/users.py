from fastapi import APIRouter, HTTPException
from src.config.db import conn
from src.models.users import users
from src.schemas.user import User
from cryptography.fernet import Fernet
from sqlalchemy.sql import select, insert, update, delete

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)


@user.get('/', tags=['users'])
async def get_users():
    stmt = select(users)
    result = conn.execute(stmt).fetchall()
    users_list = [dict(row._mapping) for row in result]
    return {'msg': 'Get Users', 'data': users_list}


@user.get('/{user_id}', tags=['users'])
async def read_user(user_id: int):
    stmt = select(users).where(users.c.id == user_id)
    result = conn.execute(stmt).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {'msg': f'Read User {user_id}', 'data': dict(result._mapping)}


@user.post('/', tags=['users'])
async def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user['password'] = f.encrypt(user.password.encode("utf-8"))
    stmt = insert(users).values(new_user)
    result = conn.execute(stmt)
    conn.commit()
    return {'msg': 'User created', 'id': result.inserted_primary_key[0]}


@user.put('/{user_id}', tags=['users'])
async def update_user(user_id: int, user: User):
    stmt = select(users).where(users.c.id == user_id)
    result = conn.execute(stmt).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = {"name": user.name, "email": user.email}
    if user.password:
        updated_user['password'] = f.encrypt(user.password.encode("utf-8"))

    stmt = update(users).where(users.c.id == user_id).values(updated_user)
    conn.execute(stmt)
    conn.commit()
    return {'msg': f'User {user_id} updated'}


@user.delete('/{user_id}', tags=['users'])
async def delete_user(user_id: int):
    stmt = select(users).where(users.c.id == user_id)
    result = conn.execute(stmt).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")

    stmt = delete(users).where(users.c.id == user_id)
    conn.execute(stmt)
    conn.commit()
    return {'msg': f'User {user_id} deleted'}
