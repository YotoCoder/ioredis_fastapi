
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import aioredis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/temp')
async def temp():
    redis = aioredis.from_url("redis://localhost")
   
    value = await redis.get('temp')
    
    return value

