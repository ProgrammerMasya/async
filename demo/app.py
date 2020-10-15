import asyncpgsa

from aiohttp import web

from .routes import setup_routes


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    # app.on_startup.append(on_start)
    # app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']
    if config.get('database_uri'):
        app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])


async def on_shutdown(app):
    await app['db'].close()
