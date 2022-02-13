import httpx
import pytest
from fastapi import status

create_book_payload = dict(
    title="Dune",
    author="Frank Herbert",
    category="have_read",
    book_link="https://www.goodreads.com/book/show/44767458-dune",
    image_link="https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1555447414l/44767458.jpg"
)


def run_book_asserts(json: dict, payload: dict, book_id: int | None = None) -> None:
    assert json["title"] == payload["title"]
    assert json["author"] == payload["author"]
    assert json["category"] == payload["category"]
    assert json["book_link"] == payload["book_link"]
    assert json["image_link"] == payload["image_link"]
    if not book_id:
        assert json["id"] is not None
    else:
        assert json["id"] == book_id


@pytest.mark.asyncio
async def test_create_book(client: httpx.AsyncClient):
    response = await client.post("/books", json=create_book_payload)
    json = response.json()

    run_book_asserts(json, create_book_payload)


@pytest.mark.asyncio
async def test_create_book_incomplete(client: httpx.AsyncClient):
    """No author"""
    payload = create_book_payload.copy()
    del payload["author"]
    response = await client.post("/books", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_book_invalid(client: httpx.AsyncClient):
    """Title is invalid"""
    payload = create_book_payload.copy()
    payload["title"] = ""
    response = await client.post("/books", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_read_books(client: httpx.AsyncClient):
    payload_1 = create_book_payload.copy()
    payload_2 = create_book_payload.copy()
    payload_2["title"] = "Dune Messiah"

    response = await client.post("/books", json=payload_1)
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post("/books", json=payload_2)
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.get("/books")
    json = response.json()

    assert response.status_code == status.HTTP_200_OK

    assert len(json) == 2
    run_book_asserts(json[0], payload_1)
    run_book_asserts(json[1], payload_2)


@pytest.mark.asyncio
async def test_read_book(client: httpx.AsyncClient):
    response = await client.post("/books", json=create_book_payload)
    assert response.status_code == status.HTTP_201_CREATED

    book_id = response.json()["id"]

    response = await client.get(f"/books/{book_id}")
    json = response.json()

    run_book_asserts(json, create_book_payload, book_id=book_id)


@pytest.mark.asyncio
async def test_update_book(client: httpx.AsyncClient):
    response = await client.post("/books", json=create_book_payload)
    assert response.status_code == status.HTTP_201_CREATED

    book_id = response.json()["id"]
    payload = create_book_payload.copy()
    payload["title"] = "Dune Messiah"

    response = await client.patch(f"/books/{book_id}", json=dict(title=payload["title"]))
    json = response.json()

    run_book_asserts(json, payload, book_id=book_id)


@pytest.mark.asyncio
async def test_delete_book(client: httpx.AsyncClient):
    response = await client.post("/books", json=create_book_payload)
    assert response.status_code == status.HTTP_201_CREATED

    book_id = response.json()["id"]

    response = await client.delete(f"/books/{book_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = await client.get(f"/books/{book_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
