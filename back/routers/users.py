from http import HTTPStatus

from fastapi import APIRouter

from back.database.database import client
from back.schemas.users import UserSchema, UserList

router = APIRouter(prefix='/users', tags=['users'])

@router.get('/', response_model=UserList)
def get_users():
    users = client.get_users()
    return {'users': users}

@router.get('/{user_id}', response_model=UserSchema)
def get_user(user_id: str):
    user = client.get_user(user_id)
    return user