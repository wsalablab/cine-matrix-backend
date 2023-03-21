from app.api.models import AuthenticationIn, AuthenticationOut, AuthenticationUpdate
from app.api.db import authentication, database


async def add_authentication(payload: AuthenticationIn):
    query = authentication.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_authentication(id):
    query = authentication.select(authentication.c.id==id)
    return await database.fetch_one(query=query)