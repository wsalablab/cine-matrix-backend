from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import UserGroup, UsergroupOut, UsergroupIn, UsergroupUpdate, GroupOut, GroupIn
from app.api import db_manager
from app.api.service import is_user_present

usergroup = APIRouter()

@usergroup.post('/usergroup/', response_model=UsergroupOut, status_code=201)
async def create_usergroup(payload: UsergroupIn):
    usergroup_id = await db_manager.add_usergroup(payload)
    response = {
        'id': usergroup_id,
        **payload.dict()
    }
    return response

@usergroup.get('/usergroup/{id}/', response_model=UsergroupOut)
async def get_usergroup(id: int):
    usergroup = await db_manager.get_usergroup(id)
    if not usergroup:
        raise HTTPException(status_code=404, detail="usergroup not found")
    return usergroup

#@usergroup.get('/movie_genres/', response_model=List[MovieGenreIn])
#async def get_movie_genresss():
#    return await db_manager.get_all_movie_genresss()

@usergroup.post('/group/', response_model=GroupOut, status_code=201)
async def create_group(payload: GroupIn):
    group_id = await db_manager.add_group(payload)
    response = {
        'id': group_id,
        **payload.dict()
    }
    return response

@usergroup.get('/group/{id}/', response_model=GroupOut)
async def get_group(id: int):
    group = await db_manager.get_group(id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

#http://localhost:8080/api/v1/usergroup/groups/
@usergroup.get('/groups/', response_model=List[GroupOut])
async def get_groups():
    groups = await db_manager.get_groups()
    if not groups:
        raise HTTPException(status_code=404, detail="Groups not found")
    return groups

@usergroup.get('/test/{id}/', response_model=GroupOut)
async def get_test(id: int):
    if (is_user_present(id)) :
        new_cast = GroupOut(id=1, name="John Doe")
        return new_cast
    else :
        new_cast = GroupOut(id=2, name="John Wick")
        return new_cast
        
@usergroup.post('/user-group/', response_model=GroupOut)
async def set_usergroup(payload: UserGroup):
    if(is_user_present(payload.id_user) and db_manager.isGroupPresent(payload.id_group)) :
        new_cast = GroupOut(id=1, name="John Doe")
        return new_cast
    else :
        new_cast = GroupOut(id=2, name="John Wick")
        return new_cast


