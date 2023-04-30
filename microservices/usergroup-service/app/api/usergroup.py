from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import UserGroup, GroupOut, GroupIn
from app.api import db_manager
from app.api.service import is_user_present

usergroup = APIRouter()

@usergroup.post('/group/', response_model=GroupOut, status_code=201)
async def create_group(payload: GroupIn):
    if await db_manager.isGroupNameUsed(payload.name) :
        raise HTTPException(status_code=403, detail="Group name already used")
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

@usergroup.delete('/delete-group/{id}')
async def delete_group(id: int):
    group = await db_manager.get_group(id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    usergroups: List[UserGroup] = await db_manager.get_user_groups_by_id_group(id)
    if usergroups is None :
        raise HTTPException(status_code=404, detail="Error Usergroup none")
    if len(usergroups) > 0 :
        await db_manager.delete_user_group_by_id_group(id)
    await db_manager.delete_group(id)

@usergroup.post('/usergroup/')
async def add_usergroup(payload: UserGroup):
    if not is_user_present(payload.id_user) :
        raise HTTPException(status_code=404, detail="User not found")
    if not await db_manager.isGroupPresent(payload.id_group) :
        raise HTTPException(status_code=404, detail="Group not found")
    userGroup = await db_manager.get_user_group(id_user=payload.id_user, id_group=payload.id_group)
    if not userGroup is None :
        raise HTTPException(status_code=403, detail="User already a group member")
    await db_manager.add_user_group(payload)

@usergroup.delete('/usergroup/')
async def delete_usergroup(payload: UserGroup):
    usergroup = await db_manager.get_user_group(id_user=payload.id_user, id_group=payload.id_group)
    if not usergroup:
        raise HTTPException(status_code=404, detail="User not found in group")
    await db_manager.delete_user_group(id_user=payload.id_user, id_group=payload.id_group)

@usergroup.get('/usergroups/', response_model=List[UserGroup])
async def get_usergroups():
    usergroups = await db_manager.get_all_user_groups()
    if usergroups is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve usegroups")
    return usergroups

@usergroup.get('/usergroups/{id}')
async def get_usergroups(id: int):
    usergroups = await db_manager.get_user_groups_by_id_user(id)
    if usergroups is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve usegroups")
    if len(usergroups) > 0 :
        return True
    return False

@usergroup.get('/test/')
async def test_usg():
    return True

