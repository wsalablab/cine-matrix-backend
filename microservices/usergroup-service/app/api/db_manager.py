from app.api.models import UsergroupIn, UsergroupOut, UsergroupUpdate
from app.api.db import usergroup, database


async def add_usergroup(payload: UsergroupIn):
    query = usergroup.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_usergroup(id):
    query = usergroup.select(usergroup.c.id==id)
    return await database.fetch_one(query=query)