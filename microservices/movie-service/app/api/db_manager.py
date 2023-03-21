from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api.db import movie, database


async def add_movie(payload: MovieIn):
    query = movie.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_movie(id):
    query = movie.select(movie.c.id==id)
    return await database.fetch_one(query=query)