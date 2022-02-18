import httpx
import pytest
from tortoise.exceptions import DoesNotExist

from app.data.models.book import BookDB


@pytest.mark.asyncio
async def test_get_by_id_does_not_exist(client: httpx.AsyncClient):
    with pytest.raises(DoesNotExist):
        await BookDB.get(id=1)
