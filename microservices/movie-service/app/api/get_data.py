# Importation des modules nécessaires
from typing import List, Optional
import requests
import json
import pandas as pd
from models import MovieInGenreNew, GenreInNew, LastMovieInGenre

from time import strftime
# pour récuperer la date du jour 
print("TIME : " + strftime("%Y/%m/%d"))

# Définition des URLs de l'API et de la clé API
API_key = '2a35719d0d9b5e5907c67db8eb374dff'

Movie_POPULAR_URL = 'https://api.themoviedb.org/3/movie/popular?api_key=' + \
    API_key + '&language=fr-FR&page='

Genre_MOVIE_URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + \
    API_key + '&language=fr-FR'

Last_MOVIE_URL = 'https://api.themoviedb.org/3/movie/changes?api_key=' + \
    API_key + '&language=fr-FR'


API_GET_MOVIE_URL = 'https://api.themoviedb.org/3/movie/'


# Fonction pour récupérer les données de films à partir de l'API
def get_movie_data_api(url, page) -> List[MovieInGenreNew]:
    response = requests.get(url + str(page))
    if response.status_code == 200:
        array = response.json()
        movies = []
        for item in array['results']:
            # Création d'une instance de MovieInGenreNew à partir des données JSON de l'API
            movie = MovieInGenreNew(**item)
            # Récupération des IDs de genres du film
            movie_genre_ids = movie.get_genre_ids()
            # Ajout des données du film dans une liste
            movies.append({
                'id': movie.id,
                'title': movie.title,
                'poster_path': movie.poster_path,
                'overview': movie.overview,
                'genre_ids': movie_genre_ids
            })
        return movies
    else:
        return 'error'

# Fonction pour récupérer les données de genres à partir de l'API
def get_genre_data_api(url) -> List[GenreInNew]:
    response = requests.get(url)
    if response.status_code == 200:
        array = response.json()
        genres = []
        for item in array['genres']:
            # Création d'une instance de GenreInNew à partir des données JSON de l'API
            genre = GenreInNew(**item)
            # Ajout des données du genre dans une liste
            genres.append({
                'id': genre.id,
                'name': genre.name
            })
        return genres
    else:
        return 'error'
    
# Fonction pour récupérer les id des dernier movie ajouté à partir de l'API
def get_last_movie_id(url) -> List[int]:
    response = requests.get(url)
    if response.status_code == 200:
        array = response.json()
        list_id_movies = []
        for item in array['results']:
           list_id_movies.append(item['id'])
        return list_id_movies
    else:
        return 'error'

# Filtrer les films qui ne sont pas dans la base de données
def check_movie_ids_not_in_data(movies: List[MovieInGenreNew], movies_id: List[int]) -> List[int]:
    # Récupère les ids des films dans la liste movies
    movie_ids = [movie['id'] for movie in movies]
    # Filtre les ids de movies_id qui ne sont pas présents dans movie_ids
    filtered_ids = list(filter(lambda x: x not in movie_ids, movies_id))
    return filtered_ids

# Fonction pour écrire les données de films dans un fichier JSON
def write_file(filename, text):
    dataset = json.loads(text)
    with open(filename, 'a') as json_file:
        try:
            collection_name = dataset['belongs_to_collection']['name']
        except KeyError:
            collection_name = None
        movie_genre_ids = dataset['genre_ids']
        result = {
            'original_title': dataset['original_title'],
            'collection_name': collection_name,
            'genre_ids': movie_genre_ids
        }
        json.dump(result, json_file)
        print(result)

# Fonction pour récupérer les données de films à partir de l'API
def get_movie_data_api_by_id(url, movies_id: List) -> List[LastMovieInGenre]:
    movies = []
    for movie_id in movies_id:
        response = requests.get(url + str(movie_id) + '?api_key=' + API_key + '&language=fr-FR')
        print(' response.status_code : ' + str(response.status_code))
        list_id_genres_movies = []
        if response.status_code == 200:
            print('dans le if')
            array = response.json()
            movie = LastMovieInGenre(**array)

            movie_genre_ids = movie.get_genre_ids()
            list_id_genres_movies = [movie_genre_id['id'] for movie_genre_id in movie_genre_ids] 

            movies.append({
                'id': movie.id,
                'title': movie.title,
                'poster_path': movie.poster_path,
                'overview': movie.overview,
                'genres' : list_id_genres_movies

            })
    return movies

# Fonction pour récupérer les données de films sur les 100 pages de l'API
def get_movie_data() -> List:
    movie = []
    for i in range(1, 100):
        movies = get_movie_data_api(Movie_POPULAR_URL, i)
        if movies == "error":
            break
        movie.extend(movies)
    return movie

# Exporte les données de films dans un fichier JSON 
def export_data_movie_to_json(movie):
    all_movies = pd.DataFrame(movie)
    # Ajouter le film dans un json
    with open('./assets/movie_collection_data.json', 'w') as f:
        json.dump(all_movies.to_dict(orient='records'), f)
    
    # obtenir les données de genre de l'API, convertir en dataframe pandas et écrire dans le fichier JSON
    genres = get_genre_data_api(Genre_MOVIE_URL)
    all_genres = pd.DataFrame(genres)
    with open('./assets/genre_data.json', 'w') as f:
        json.dump(all_genres.to_dict(orient='records'), f)



#async def add_movie(payload: MovieInGenreNew):
#    query = movies.insert().values(**payload.dict())
#    return await database.execute(query=query)

if __name__ == '__main__':
    movie = get_movie_data()
    #add_movie(movie[0])
    #print(movie)

    # export_data_movie_to_json(movie) # exporte les données de films dans un fichier JSON 

    # main pour vérifier 
    # new_id = check_movie_ids_not_in_data(movie, get_last_movie_id(Last_MOVIE_URL))
    # data = get_movie_data_api_by_id(API_GET_MOVIE_URL, new_id)
