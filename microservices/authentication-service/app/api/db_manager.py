from fastapi import HTTPException
from app.api.models import UserIn, UserInTokenExp
from app.api.db import database, user


#async def add_authentication(payload: AuthenticationIn):
#    query = authentication.insert().values(**payload.dict())
#    return await database.execute(query=query)

#async def get_authentication(id):
#    query = authentication.select(authentication.c.id==id)
#    return await database.fetch_one(query=query)

async def add_user(payload: UserIn):
    if await get_user_by_mail(payload.mail) == 1 :
        raise HTTPException(status_code=409, detail="Email already registered")
    else :
        query = user.insert().values(**payload.dict(), token_exp=30)
        return await database.execute(query=query)

async def get_user(id):
    query = user.select(user.c.id==id)
    return await database.fetch_one(query=query)

async def get_user_by_mail(mail) -> int :
    query = user.select(user.c.mail==mail)
    result = await database.fetch_one(query=query)
    return 1 if result else 0

async def delete_user(id: int):
    query = user.delete().where(user.c.id==id)
    return await database.execute(query=query)

async def get_all_utilisateurs():
    query = user.select()
    return await database.fetch_all(query=query)