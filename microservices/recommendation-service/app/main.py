from fastapi import FastAPI
from app.api.recommendation import recommendation
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/recommendation/openapi.json", docs_url="/api/v1/recommendation/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(recommendation, prefix='/api/v1/recommendation', tags=['recommendation'])
