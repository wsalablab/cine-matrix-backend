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