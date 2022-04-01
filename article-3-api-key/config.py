from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = ".env.sample"

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()