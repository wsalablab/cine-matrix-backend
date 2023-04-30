from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import UserOut, UserIn
from app.api import db_manager
from app.api import service

authentication = APIRouter()

@authentication.post('/user/', response_model=int, status_code=201)
async def create_user(payload: UserIn):
    user_id = await db_manager.add_user(payload)
    return user_id

@authentication.get('/user/{id}/', response_model=UserOut)
async def get_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        #raise HTTPException(status_code=404, detail="User not found")
        raise HTTPException(status_code=400, detail="BAD REQUEST")
    return user

@authentication.delete('/user/{id}/')
async def delete_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    service.delete_movies_user(id)
    service.delete_groups_user(id)
    await db_manager.delete_user(id)

#http://localhost:8080/api/v1/authentication/users/
@authentication.get('/users/', response_model=List[UserOut])
async def get_users():
    return await db_manager.get_all_utilisateurs()

@authentication.get('/test/')
async def test_usg():
    return service.test_usergroup()

@authentication.get('/testmovie/')
async def test_movie():
    return service.test_movie()