import random
import asyncio
import time
import aioredis
from conf.settings import URL_DATABASE

async def main():
    while True:
        try:
            redis = await aioredis.from_url(URL_DATABASE)
            async with redis.pipeline(transaction=True) as pipe:
                ok1, ok2, ok3 = await (
                                        pipe.set("id", random.randint(1,100))
                                        .set("temp", random.randint(1,100))
                                        .set("humidity", random.randint(1,100))
                                        .execute()
                                    )
                id = await redis.get('id')
                temp = await redis.get('temp')
                hum = await redis.get('humidity')
                print(f'ID: {int(id)}\nTemp: {int(temp)}\nHumidity: {int(hum)}\n\n')

            assert ok1
            assert ok2
            assert ok3
        except Exception as e:
            print(e)

        time.sleep(1)
        
        
         
    
if __name__ == "__main__":
    asyncio.run(main())