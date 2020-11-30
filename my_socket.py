"""
Fourth homework assignment in the course "Python".

Created by Emdin Grigory.
"""


import aiohttp
from aiohttp import web


async def client(number):
    """
    Send  a request to https://jsonplaceholder.typicode.com/todos/number.

    Args:
        number: number for request.

    Returns:
        response.
    """
    async with aiohttp.ClientSession() as session:
        address = 'https://jsonplaceholder.typicode.com/todos/'
        address += number
        async with session.get(address) as resp:
            return await resp.read(), resp.status, resp.headers


async def server(request):
    """
    Server.

    Args:
        request: request to the server.

    Returns:
        response.
    """
    number = request.match_info.get('number')
    raw, status, headers = await client(number)
    return web.Response(status=status, headers=headers, body=raw)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/todo/{number}', server)])
    web.run_app(app)
