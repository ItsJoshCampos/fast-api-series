# app.py
from fastapi import FastAPI

from config import settings

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello world" }


@app.get("/vars")
async def info():
    return {
        "default variable": settings.DEFAULT_VAR,
        "api key": settings.API_KEY,
        "app max integer": settings.APP_MAX,
    }