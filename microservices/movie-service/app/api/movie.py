from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import AppreciationIn ,MovieIn, MovieUpdate, GenreIn, GenreUpdate, MovieGenreIn, MovieGenreUpdate, MovieInGenre, MovieInUpdate, MovieSearch, MovieWatch, DateInDb, Appreciation
from app.api import db_manager
from app.api import service
from app.api import get_dataa as tmdb
from time import strftime


movie = APIRouter()

@movie.get('/test/', response_model=List[MovieGenreIn])
async def get_moviesss():
    return await db_manager.get_movie_genre_by_movie(27)

@movie.post('/testtt/{id}')
async def get_testtt(id: int, payload: MovieInUpdate):
    print("a")
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    print("b")
    if payload.genres is not None and (len(payload.genres) >= 0):
        print("c")
        #on met a jour
        print(movie)
        moviegenres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(id)
        print("d")
        print(moviegenres)  
       
        if len(moviegenres) > 0 :
            print("e")
            for moviegenre in moviegenres:
                print("on delete le genre")
                await db_manager.delete_movie_genre(id_movie=id, id_genre=moviegenre.id_genre)
        if len(payload.genres) > 0 :
            for genre_id in payload.genres:
                print("on cree le genre")
                new_movie_genre_in: MovieGenreIn = MovieGenreIn(id, genre_id)
                await db_manager.add_movie_genre(new_movie_genre_in)
    
    new_movie_dict = payload.dict(exclude={'genres'}, exclude_unset=True)

    has_non_null_element = False
    for k, v in new_movie_dict.items():
        if k != 'genres' and v is not None:
            has_non_null_element = True
            break

    if has_non_null_element :
        new_movie = MovieUpdate(**new_movie_dict)
        await db_manager.update_movie(id, new_movie)


@movie.get('/movies/', response_model=List[MovieInGenre])
async def get_moviesss():
    movies: List[MovieIn] = await db_manager.get_all_moviesss()
    moviesin: List[MovieInGenre] = []
    for movie in movies:
        new_genres: List[int] = []
        movies_genres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(movie.id_tdmb)
        for movie_genre in movies_genres:
            new_genres.append(movie_genre.id_genre)
        movieInGenre = MovieInGenre(id_tdmb=movie.id_tdmb, title=movie.title, poster=movie.poster, synopsis=movie.synopsis, genres=new_genres) 
        moviesin.append(movieInGenre)
    return moviesin

@movie.post('/movie-search/', response_model=List[MovieInGenre])
async def search_movie_by_title(payload: MovieSearch):
    movies: List[MovieIn] = await db_manager.search_movies("a")
    moviesin: List[MovieInGenre] = []
    for movie in movies:
        new_genres: List[int] = []
        movies_genres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(movie.id_tdmb)
        for movie_genre in movies_genres:
            new_genres.append(movie_genre.id_genre)
        movieInGenre = MovieInGenre(id_tdmb=movie.id_tdmb, title=movie.title, poster=movie.poster, synopsis=movie.synopsis, genres=new_genres) 
        moviesin.append(movieInGenre)
    return moviesin

@movie.get('/movies/page/{page}/', response_model=List[MovieInGenre])
async def get_movies_page(page: int):
    count = await db_manager.count_movies()
    elements_per_page = 2
    max_page: int = (count/elements_per_page)
    if(count % elements_per_page):
        max_page+=1
    if(page < 1 or page > max_page):
        raise HTTPException(status_code=404, detail="Page not found")
    limit = 2
    offset = ((page - 1) * limit)    
    movies = await db_manager.get_movies_with_limit_offset(limit, offset)
    moviesin: List[MovieInGenre] = []
    for movie in movies:
        new_genres: List[int] = []
        movies_genres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(movie.id_tdmb)
        for movie_genre in movies_genres:
            new_genres.append(movie_genre.id_genre)
        movieInGenre = MovieInGenre(id_tdmb=movie.id_tdmb, title=movie.title, poster=movie.poster, synopsis=movie.synopsis, genres=new_genres) 
        moviesin.append(movieInGenre)
    return moviesin

@movie.post('/movie/', status_code=201)
async def create_moviein(payload: MovieInGenre):
    
    for genre_id in payload.genres:
        genre = db_manager.get_genre(genre_id)
        if not genre :
            raise HTTPException(status_code=404, detail="Genre not found" + genre_id)
        
    movie = MovieIn(id_tdmb=payload.id_tdmb, title=payload.title, poster=payload.poster, synopsis=payload.synopsis)
    await db_manager.add_movie(movie)
    
    for genre_id in payload.genres:
        movie_genre = await db_manager.get_movie_genre(payload.id_tdmb, genre_id)
        if not movie_genre :
            new_movie_genre = MovieGenreIn(id_movie=payload.id_tdmb, id_genre=genre_id)
            await db_manager.add_movie_genre(new_movie_genre)


@movie.get('/movie/{id}/', response_model=MovieInGenre)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    new_genres: List[int] = []
    movies_genres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(movie.id_tdmb)
    for movie_genre in movies_genres:
        new_genres.append(movie_genre.id_genre)
    movieInGenre = MovieInGenre(id_tdmb=movie.id_tdmb, title=movie.title, poster=movie.poster, synopsis=movie.synopsis, genres=new_genres) 
    return movieInGenre

@movie.delete('/movie/{id}/')
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    moviegenres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(id)
    if len(moviegenres) > 0 :
        for moviegenre in moviegenres:
            await db_manager.delete_movie_genre(id_movie=id, id_genre=moviegenre.id_genre)
    
    await db_manager.delete_movie(id)

@movie.post('/movie/{id}/')
async def update_movie(id: int, payload: MovieInUpdate):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    if payload.genres is not None and (len(payload.genres) >= 0):
        moviegenres: List[MovieGenreIn] = await db_manager.get_movie_genre_by_movie(id)
        genres: List[int] = payload.genres
        if len(moviegenres) > 0 :
            for moviegenre in moviegenres:
                await db_manager.delete_movie_genre(id_movie=id, id_genre=moviegenre.id_genre)
        
        if len(genres) > 0 :
            for genre_id in genres:
                new_movie_genre_in: MovieGenreIn = MovieGenreIn(id_movie=id, id_genre=genre_id)
                await db_manager.add_movie_genre(new_movie_genre_in)
    
    new_movie_dict = payload.dict(exclude={'genres'}, exclude_unset=True)

    has_non_null_element = False
    for k, v in new_movie_dict.items():
        if k != 'genres' and v is not None:
            has_non_null_element = True
            break

    if has_non_null_element :
        new_movie = MovieUpdate(**new_movie_dict)
        await db_manager.update_movie(id, new_movie)

@movie.post('/genre/', response_model=GenreIn, status_code=201)
async def create_genre(payload: GenreIn):
    await db_manager.add_genre(payload)
    response = {
        **payload.dict()
    }
    return response

@movie.get('/genres/', response_model=List[GenreIn])
async def get_genresss():
    return await db_manager.get_all_genresss()

@movie.get('/genre/{id}/', response_model=GenreIn)
async def get_genre(id: int):
    genre = await db_manager.get_genre(id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@movie.post('/genre/{id}/')
async def update_genre(id: int, payload: GenreUpdate):
    genre = await db_manager.get_genre(id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    db_manager.update_genre(id, payload)

@movie.delete('/genre/{id}/')
async def delete_genre(id: int):
    genre = await db_manager.get_genre(id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    await db_manager.delete_genre(id)

@movie.post('/movie_genre/', response_model=MovieGenreIn, status_code=201)
async def create_movie_genre(payload: MovieGenreIn):
    genre = await db_manager.get_genre(payload.id_genre)
    if not genre :
        raise HTTPException(status_code=404, detail="Genre not found")
    movie = await db_manager.get_movie(payload.id_movie)
    if not movie :
        raise HTTPException(status_code=404, detail="Movie not found")
    movie_genre = await db_manager.get_movie_genre(payload.id_movie, payload.id_genre)
    if movie_genre :
        raise HTTPException(status_code=409, detail="Movie_genre already existing")
    await db_manager.add_movie_genre(payload)
    response = {
        **payload.dict()
    }
    return response

@movie.get('/movie_genre/{id_movie}/', response_model=List[MovieGenreIn])
async def get_movie_genres(id_movie: int):
    return await db_manager.get_movie_genres(id_movie)

@movie.delete('/movie_genre/{id_movie}/{id_genre}/')
async def delete_movie_genre(id_movie: int, id_genre: int):
    movie_genre = await db_manager.get_movie_genre(id_movie, id_genre)
    if not movie_genre:
        raise HTTPException(status_code=404, detail="Movie genre not found")
    await db_manager.delete_movie_genre(id_movie, id_genre)

@movie.get('/movie_genres/', response_model=List[MovieGenreIn])
async def get_movie_genresss():
    return await db_manager.get_all_movie_genresss()

@movie.get('/test/')
async def test_usg():
    return True

@movie.post('/appreciation/')
async def add_appreciation(payload: AppreciationIn):
    appreciation = await db_manager.get_appreciation_by_name(payload.name)
    if appreciation:
        raise HTTPException(status_code=404, detail="Appreciation name already used")
    appreciation_id = await db_manager.add_appreciation(payload)
    response = {
        'id': appreciation_id,
        **payload.dict()
    }
    return response

@movie.get('/appreciation/{id}/', response_model=Appreciation)
async def get_appreciation(id: int):
    appreciation = await db_manager.get_appreciation(id)
    if not appreciation:
        raise HTTPException(status_code=404, detail="Appreciation not found")
    return appreciation

@movie.delete('/appreciation/{id}/')
async def delete_appreciation(id: int):
    appreciation = await db_manager.get_appreciation(id)
    if not appreciation:
        raise HTTPException(status_code=404, detail="Appreciation not found")
    return await db_manager.delete_appreciation(id)

@movie.get('/movie_watch_user/{id}', response_model=List[MovieWatch])
async def get_movie_watch_by_user(id: int):
    movies_watched = await db_manager.get_movies_watched_by_user(id)
    if movies_watched is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve movies watched")
    return movies_watched

@movie.delete('/movie_watch/{id_movie}/{id_user}/')
async def delete_movie_watch(id_movie: int, id_user: int):
    movie_watch = await db_manager.get_movie_watch(id_movie=id_movie, id_user=id_user)
    if not movie_watch:
        raise HTTPException(status_code=404, detail="Movie watched not found")
    return await db_manager.delete_movie_watch(id_user=id_user, id_movie=id_movie)

@movie.get('/appreciations/', response_model=List[Appreciation])
async def get_appreciations():
    appreciations: List[Appreciation] = await db_manager.get_all_appreciation()
    if appreciations is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve appreciations")
    return appreciations

@movie.get('/movies_watched/', response_model=List[MovieWatch])
async def get_movies_watched():
    movies_watched: List[MovieWatch] = await db_manager.get_all_movie_watch()
    if movies_watched is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve movies watched")
    return movies_watched

@movie.post('/movie_watch/')
async def add_movie_watch(payload: MovieWatch):
    movie = await db_manager.get_movie(payload.id_movie)
    if not movie :
        raise HTTPException(status_code=404, detail="Failed to retrieve movie")
    if not service.is_user_present(payload.id_user):
        raise HTTPException(status_code=404, detail="Failed to retrieve user")
    appreciation = await db_manager.get_appreciation(id=payload.id_appreciation)
    if not appreciation:
        raise HTTPException(status_code=404, detail="Failed to retrieve appreciation")
    
    movie_watch = await db_manager.get_movie_watch(id_user=payload.id_user, id_movie=payload.id_movie)
    if not movie_watch :
        await db_manager.add_movie_watch(payload)
    

@movie.get('/update_tdmb/')
async def updateadd_movie_watch_tdmb():
    movie = tmdb.chech_movie_update()
    return True

@movie.get('/update_date/')
async def update_date(payload: DateInDb):
    date = await db_manager.get_date()
    if not date:
        raise HTTPException(status_code=404, detail="Movie not found")
    else:
        new_date = DateInDb(**payload)
        await db_manager.update_movie(new_date)