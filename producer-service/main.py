import random
import asyncio
import aioredis

async def main():
    while True:
        try:
            redis = await aioredis.from_url("redis://localhost")
            async with redis.pipeline(transaction=True) as pipe:
                ok1, ok2, ok3 = await (
                                        pipe.set("id", random.randint(1,100))
                                        .set("temp", random.randint(1,100))
                                        .set("humidity", random.randint(1,100))
                                        .execute()
                                    )
            assert ok1
            assert ok2
            assert ok3
        except:
            print('Ocurrio un eror...')
        
        print(f'{ok1} {ok2} {ok3}')

if __name__ == "__main__":
    asyncio.run(main())