from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import AuthenticationOut, AuthenticationIn, AuthenticationUpdate
from app.api import db_manager

authentication = APIRouter()

@authentication.post('/', response_model=AuthenticationOut, status_code=201)
async def create_authentication(payload: AuthenticationIn):
    authentication_id = await db_manager.add_authentication(payload)
    response = {
        'id': authentication_id,
        **payload.dict()
    }
    return response

@authentication.get('/{id}/', response_model=AuthenticationOut)
async def get_authentication(id: int):
    authentication = await db_manager.get_authentication(id)
    if not authentication:
        raise HTTPException(status_code=404, detail="authentication not found")
    return authentication