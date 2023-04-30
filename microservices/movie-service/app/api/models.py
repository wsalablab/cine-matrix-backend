from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    id_tdmb: int
    title: str
    poster: str
    synopsis: str

class MovieInGenre(BaseModel):
    id_tdmb: int
    title: str
    poster: str
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


class GenreInNew(BaseModel):
    id: int
    name: str

class MovieInGenreNew(BaseModel):
    id: int
    title: str
    poster_path: Optional[str]
    overview: str
    genre_ids: List[int]

    # Méthode pour récupérer les IDs de genres d'un film
    def get_genre_ids(self) -> List[int]:
        return self.genre_ids
    
class LastMovieInGenre(BaseModel):
    id: int
    title: str
    poster_path: Optional[str]
    overview: str
    genres: List

    # Méthode pour récupérer les IDs de genres d'un film
    def get_genre_ids(self) -> List[int]:
        return self.genres


class DateInDB(BaseModel):
    date: str