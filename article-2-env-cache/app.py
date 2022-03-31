from functools import lru_cache

from fastapi import Depends, FastAPI

from config import Settings

app = FastAPI()

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()

# route is now using the Depends feature to import Settings
@app.get("/vars")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "default variable": settings.DEFAULT_VAR,
        "api key": settings.API_KEY,
        "app max integer": settings.APP_MAX,
    }