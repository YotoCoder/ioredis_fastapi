
from fastapi import FastAPI
import aioredis
from conf.settings import URL_DATABASE

app = FastAPI()


@app.get('/metrics')
async def metrics():
    redis = aioredis.from_url(URL_DATABASE)
   
    id = await redis.get('id')
    temp = await redis.get('temp')
    hum = await redis.get('humidity')
 
    
    return {
                'ID': int(id),
                'Temp': int(temp),
                'Humidity': int(hum),
            }