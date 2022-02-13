import asyncio

import httpx
import pytest
from asgi_lifespan import LifespanManager

from app import create_app
from app.config import ConfigType


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(name="client")
async def client_fixture():
    app = create_app(ConfigType.TESTING)

    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            yield client
