import json
import time
import aiohttp
import asyncio


async def query():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://0.0.0.0:5000/sum', data=json.dumps({"a": 1, "b": 2})) as response:
            return await response.text()

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    tasks = [query() for i in range(1000)]
    start_time = time.time()
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
    print(time.time() - start_time)