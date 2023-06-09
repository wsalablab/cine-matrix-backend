import os
import httpx

USERGROUP_SERVICE_HOST_URL = 'http://localhost:8004/api/v1/usergroup/'
url = os.environ.get('USERGROUP_SERVICE_HOST_URL') or USERGROUP_SERVICE_HOST_URL

MOVIE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/movie/'
url_movie = os.environ.get('MOVIE_SERVICE_HOST_URL') or MOVIE_SERVICE_HOST_URL

AUTHENTICATION_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/authentication/'
url_authentication = os.environ.get('AUTHENTICATION_SERVICE_HOST_URL') or AUTHENTICATION_SERVICE_HOST_URL

def test_usergroup():
    r = httpx.get(f'{url}{"test"}')
    return True if r.status_code == 200 else False

def test_movie():
    r = httpx.get(f'{url_movie}{"test"}')
    return True if r.status_code == 200 else False

def test_authentication():
    r = httpx.get(f'{url_authentication}{"test"}') 
    return True if r.status_code == 200 else False

def is_group_exist(id: int):
    r = httpx.get(f'{url}{"group"}{id}')
    return True if r.status_code == 200 else False

def get_users_group_by_group(id : int):
    r = httpx.get(f'{url}{"usergroups-by-group"}{id}')
    return r

def get_movies_watched_by_user(id: int):
    r = httpx.get(f'{url_movie}{"movie_watch_user"}{id}')
    return r

def get_usersgroup_by_group(id: int):
    r = httpx.get(f'{url}{"usergroups-by-group"}{id}')
    return r

def get_genres_by_movie(id: int):
    r = httpx.get(f'{url_movie}{"movie_genre"}{id}')
    return r

def get_movies_by_genre(id: int):
    r = httpx.get(f'{url_movie}{"movies_by_genre"}{id}')
    return r