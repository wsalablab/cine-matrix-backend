from app.api.models import UsergroupIn, UsergroupOut, UsergroupUpdate, GroupIn
from app.api.db import usergroup, database, group


async def add_usergroup(payload: UsergroupIn):
    query = usergroup.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_usergroup(id):
    query = usergroup.select(usergroup.c.id==id)
    return await database.fetch_one(query=query)

async def add_group(payload: GroupIn):
    query = group.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_group(id):
    query = group.select(group.c.id==id)
    return await database.fetch_one(query=query)

async def get_groups():
    query = group.select()
    return await database.fetch_all(query=query)

async def isGroupPresent(id):
    group_record = await get_group(id)
    return group_record is not None