import os
import httpx

#USERGROUP_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/usergroup/user/'
#url = os.environ.get('AUTHENTICATION_SERVICE_HOST_URL') or AUTHENTICATION_SERVICE_HOST_URL

#def is_user_present(user_id: int):
#    r = httpx.get(f'{url}{user_id}')
#    return True if r.status_code == 200 else False

USERGROUP_SERVICE_HOST_URL = 'http://localhost:8004/api/v1/usergroup/'
url = os.environ.get('USERGROUP_SERVICE_HOST_URL') or USERGROUP_SERVICE_HOST_URL

MOVIE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/movie/'
url_movie = os.environ.get('MOVIE_SERVICE_HOST_URL') or MOVIE_SERVICE_HOST_URL



def test_usergroup():
    r = httpx.get(f'{url}{"test"}')
    return True if r.status_code == 200 else False

def test_movie():
    r = httpx.get(f'{url_movie}{"test"}')
    return True if r.status_code == 200 else False

def delete_movies_user(id: int):
    r = httpx.delete(f'{url_movie}{"delete_for_user"}{id}')
    return True if r.status_code == 200 else False

def delete_groups_user(id: int):
    r = httpx.delete(f'{url}{"delete_for_user"}{id}')
    return True if r.status_code == 200 else False