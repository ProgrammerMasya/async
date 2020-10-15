import asyncio
import json

from aiohttp import web

from random import randint


async def test_sum(request):
    body = await request.json()
    sum_result = int(body['a']) + int(body['b'])

    await asyncio.sleep(randint(0, 5))

    response = {'success': True, 'result': sum_result}
    return web.Response(text=json.dumps(response))
