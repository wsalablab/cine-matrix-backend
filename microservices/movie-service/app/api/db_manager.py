from typing import List
from app.api.models import MovieIn, MovieUpdate, GenreIn, GenreUpdate, MovieGenreIn
from app.api.db import movies, database, genre, movie_genre


async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_movie(id):
    query = movies.select(movies.c.id_tdmb==id)
    return await database.fetch_one(query=query)

async def delete_movie(id: int):
    query = movies.delete().where(movies.c.id_tdmb==id)
    return await database.execute(query=query)

async def update_movie(id: int, payload: MovieUpdate):
    query = (
        movies
        .update()
        .where(movies.c.id_tdmb == id)
        .values(**payload.dict(exclude_unset=True))
    )
    return await database.execute(query=query)

async def add_genre(payload: GenreIn):
    query = genre.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_genre(id):
    query = genre.select(genre.c.id==id)
    return await database.fetch_one(query=query)

async def delete_genre(id: int):
    query = genre.delete().where(genre.c.id==id)
    return await database.execute(query=query)

async def add_movie_genre(payload: MovieGenreIn):
    query = movie_genre.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_movie_genres(id_movie):
    query = movie_genre.select(movie_genre.c.id_movie==id_movie)
    return await database.fetch_all(query=query)

async def delete_movie_genre(id_movie: int, id_genre: int):
    query = movie_genre.delete().where((movie_genre.c.id_movie==id_movie) & (movie_genre.c.id_genre==id_genre))
    return await database.execute(query=query)

async def get_movie_genre(id_movie, id_genre):
    query = movie_genre.select((movie_genre.c.id_genre==id_genre) & (movie_genre.c.id_movie==id_movie))
    return await database.fetch_one(query=query)

async def get_movie_genre_by_movie(id_movie):
    query = movie_genre.select(movie_genre.c.id_movie==id_movie)
    return await database.fetch_all(query=query)

#OK
async def get_all_moviesss():
    query = movies.select()
    return await database.fetch_all(query=query)

async def get_all_genresss():
    query = genre.select()
    return await database.fetch_all(query=query)

async def get_all_movie_genresss():
    query = movie_genre.select()
    return await database.fetch_all(query=query)

async def get_movie_genre_by_movie(id_movie) -> List[MovieGenreIn]:
    query = movie_genre.select(movie_genre.c.id_movie==id_movie)
    return await database.fetch_all(query=query)

#OK
async def get_movies_with_limit_offset(limit: int, offset: int):
    query = movies.select().offset(offset).limit(limit)
    return await database.fetch_all(query=query)

async def count_movies() -> int:
    query = "SELECT COUNT(*) FROM movies_tdmb"
    result = await database.fetch_one(query)
    count = result[0]
    return count

async def search_movies(title_in: str):
    query = f"SELECT * FROM movies_tdmb where title like '%{title_in}%'"
    return await database.fetch_all(query=query)