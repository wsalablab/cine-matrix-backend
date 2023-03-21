from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import MovieOut, MovieIn, MovieUpdate
from app.api import db_manager

movie = APIRouter()

@movie.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }
    return response

@movie.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="movie not found")
    return movie