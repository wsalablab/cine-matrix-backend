from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import RecommendationOut, RecommendationIn, RecommendationUpdate
from app.api import db_manager

recommendation = APIRouter()

@recommendation.post('/recommendation/', response_model=RecommendationOut, status_code=201)
async def create_recommendation(payload: RecommendationIn):
    recommendation_id = await db_manager.add_recommendation(payload)
    response = {
        'id': recommendation_id,
        **payload.dict()
    }
    return response

@recommendation.get('/recommendation/{id}/', response_model=RecommendationOut)
async def get_recommendation(id: int):
    recommendation = await db_manager.get_recommendation(id)
    if not recommendation:
        raise HTTPException(status_code=404, detail="recommendation not found")
    return recommendation