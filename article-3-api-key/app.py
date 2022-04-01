from fastapi import Depends, FastAPI

from fastapi.security.api_key import APIKey
import auth 

app = FastAPI()

# Lockedown Route
@app.get("/secure")
async def info(api_key: APIKey = Depends(auth.get_api_key)):
    return {
        "default variable": api_key
    }

# Open Route
@app.get("/open")
async def info():
    return {
        "default variable": "Open Route"
    }