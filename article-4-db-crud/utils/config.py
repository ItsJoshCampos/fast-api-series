from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DB_UID: str
    DB_PWD: str
    DB_SERVER: str
    DB_NAME: str
    DB_PORT: int

    class Config:
        env_file = ".env.sample"

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings()