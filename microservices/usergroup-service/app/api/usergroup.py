from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import UsergroupOut, UsergroupIn, UsergroupUpdate
from app.api import db_manager

usergroup = APIRouter()

@usergroup.post('/', response_model=UsergroupOut, status_code=201)
async def create_usergroup(payload: UsergroupIn):
    usergroup_id = await db_manager.add_usergroup(payload)
    response = {
        'id': usergroup_id,
        **payload.dict()
    }
    return response

@usergroup.get('/{id}/', response_model=UsergroupOut)
async def get_usergroup(id: int):
    usergroup = await db_manager.get_usergroup(id)
    if not usergroup:
        raise HTTPException(status_code=404, detail="usergroup not found")
    return usergroup