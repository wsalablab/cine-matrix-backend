from typing import List
from app.api.models import AppreciationIn, MovieIn, MovieUpdate, GenreIn, GenreUpdate, MovieGenreIn, Appreciation, MovieWatch
from app.api.db import appreciation, movies, movie_watch, database, genre, movie_genre


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

async def get_movie_genre_by_genre(id_genre) -> List[MovieGenreIn]:
    query = movie_genre.select(movie_genre.c.id_genre==id_genre)
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

async def add_appreciation(payload: AppreciationIn):
    query = appreciation.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_appreciation(id):
    query = appreciation.select(appreciation.c.id==id)
    return await database.fetch_one(query=query)

async def delete_appreciation(id: int):
    query = appreciation.delete().where(appreciation.c.id==id)
    return await database.execute(query=query)

async def get_appreciation_by_name(name: str):
    query = appreciation.select(appreciation.c.name==name)
    return await database.fetch_one(query=query)

async def add_movie_watch(payload: MovieWatch):
    query = movie_watch.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_movie_watch(id_user: int, id_movie: int):
    query = movie_watch.select((movie_watch.c.id_user==id_user) and (movie_watch.c.id_movie==id_movie))
    return await database.fetch_one(query=query)

async def delete_movie_watch(id_user: int, id_movie: int):
    query = movie_watch.delete().where((movie_watch.c.id_user==id_user) and (movie_watch.c.id_movie==id_movie))
    return await database.execute(query=query)

async def get_movies_watched_by_user(id_user: int):
    query = movie_watch.select(movie_watch.c.id_user==id_user)
    return await database.fetch_all(query=query)

async def get_all_appreciation()-> List[Appreciation]:
    query = appreciation.select()
    return await database.fetch_all(query=query)

async def get_all_movie_watch():
    query = movie_watch.select()
    return await database.fetch_all(query=query)

async def update_movie_watch(payload: MovieWatch):
    query = (
        movie_watch
        .update()
        .where((movie_watch.c.id_user == payload.id_user) and (movie_watch.c.id_movie == payload.id_movie))
        .values(payload.id_appreciation)
    )
    return await database.execute(query=query)

#async def delete_movie_watch(id_user: int, id_movie: int):
#    query = movie_watch.delete().where((movie_watch.c.id_user==id_user) and (movie_watch.c.id_movie==id_movie))
#    return await database.execute(query=query)