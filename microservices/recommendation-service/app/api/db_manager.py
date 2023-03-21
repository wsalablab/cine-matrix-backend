from app.api.models import RecommendationIn, RecommendationOut, RecommendationUpdate
from app.api.db import recommendation, database


async def add_recommendation(payload: RecommendationIn):
    query = recommendation.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_recommendation(id):
    query = recommendation.select(recommendation.c.id==id)
    return await database.fetch_one(query=query)