import os
import httpx

AUTHENTICATION_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/authentication/user/'
url = os.environ.get('AUTHENTICATION_SERVICE_HOST_URL') or AUTHENTICATION_SERVICE_HOST_URL

def is_user_present(user_id: int):
    r = httpx.get(f'{url}{user_id}')
    return True if r.status_code == 200 else False