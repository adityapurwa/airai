import asyncio

from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from config import limiter
from helpers.external_api.meteo import Meteo
from llm import air_quality

router = APIRouter()
meteo = Meteo()


@router.get("/")
@limiter.limit("5/minute")
async def chat(request: Request):
    query = request.query_params.get("query")
    if query is None:
        raise HTTPException(status_code=400, detail="NO_QUERY")
    if len(query) > 150:
        # this is a naive check to prevent malicious queries (e.g. prompt that long enough might contains prompt
        # injection)
        raise HTTPException(status_code=400, detail="QUERY_TOO_LONG")

    cities = air_quality.air_quality_model(query)

    if cities is None:
        raise HTTPException(status_code=400, detail="NOT_ASKING_ABOUT_AIR_QUALITY")

    if len(cities) == 0:
        return {
            "air_qualities": None,
        }

    coroutines = []

    # we want to fetch the air quality for all cities concurrently as they don't depend on each other
    for city in cities:
        coroutine = meteo.fetch_air_quality(city)
        coroutines.append(coroutine)

    air_qualities = await asyncio.gather(*coroutines)

    return {
        "air_qualities": air_qualities,
    }
