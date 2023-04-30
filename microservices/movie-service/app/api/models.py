import datetime
from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    id_tdmb: int
    title: str
    poster: Optional[str]
    synopsis: str

class MovieInGenre(BaseModel):
    id_tdmb: int
    title: str
    poster: Optional[str]
    synopsis: str
    genres: List[int]

class MovieInUpdate(BaseModel):
    title: Optional[str] = None
    poster: Optional[str] = None
    synopsis: Optional[str] = None
    genres: List[int] = None

    
#class MovieOut(MovieIn):
#    id: int

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    poster: Optional[str] = None
    synopsis: Optional[str] = None
    


class GenreIn(BaseModel):
    id: int
    name: str

class GenreUpdate(GenreIn):
    id: Optional[int] = None
    name: Optional[str] = None

class MovieGenreIn(BaseModel):
    id_movie: int
    id_genre: int

class MovieGenreUpdate(MovieGenreIn):
    id_movie: Optional[int] = None
    id_genre: Optional[int] = None

class MovieSearch(BaseModel):
    title: str

class AppreciationIn(BaseModel):
    name: str

class Appreciation(BaseModel):
    id: int
    name: str

class MovieWatch(BaseModel):
    id_user: int
    id_movie: int
    id_appreciation: int

class DateInDb(BaseModel):
    id: int
    date_update : str