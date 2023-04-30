from app.api.models import UsergroupIn, UsergroupOut, UsergroupUpdate, GroupIn, UserGroup
from app.api.db import usergroup, database, group, user_group


async def add_usergroup(payload: UsergroupIn):
    query = usergroup.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_usergroup(id):
    query = usergroup.select(usergroup.c.id==id)
    return await database.fetch_one(query=query)

#Debut

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

async def isGroupNameUsed(name: str):
    query = group.select(group.c.name==name)
    group_record = await database.fetch_one(query=query)
    return group_record is not None

async def delete_group(id: int):
    query = group.delete().where(group.c.id==id)
    return await database.execute(query=query)

async def get_user_groups_by_id_user(id):
    query = user_group.select(user_group.c.id_user==id)
    return await database.fetch_all(query=query)

async def get_user_groups_by_id_group(id):
    query = user_group.select(user_group.c.id_group==id)
    return await database.fetch_all(query=query)

async def get_user_group(id_user: int, id_group: int):
    query = user_group.select((user_group.c.id_user==id_user) and (user_group.c.id_group==id_group))
    return await database.fetch_one(query=query)

async def add_user_group(payload: UserGroup):
    query = usergroup.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_user_groups():
    query = user_group.select()
    return await database.fetch_all(query=query)

async def delete_user_group(id_user: int, id_group: int):
    query = user_group.delete().where((user_group.c.id_user==id_user) and (user_group.c.id_group==id_group))
    return await database.execute(query=query)

async def delete_user_group_by_id_group(id_group: int):
    query = user_group.delete().where(user_group.c.id_group==id_group)
    return await database.execute(query=query)