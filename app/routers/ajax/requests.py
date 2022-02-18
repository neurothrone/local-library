import httpx
from fastapi import Request, Query

from app.routers.library.models import BookOut


async def create_book_with_form_data(request: Request,
                                     payload: dict
                                     ) -> BookOut:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=request.url_for("create_book"),
            json=payload)

    return BookOut(**response.json())


async def search_for_books_by(request: Request,
                              text: str = Query(default=""),
                              ) -> list[BookOut]:
    if not text:
        return []

    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=request.url_for("read_books_ilike_by"),
            params=dict(query=text))
        books = response.json()

    return [BookOut(**data) for data in books]


async def get_book_by_id(request: Request,
                         book_id: int) -> BookOut:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=request.url_for("read_book", book_id=book_id))

    return BookOut(**response.json())


async def update_book_by_id(request: Request,
                            book_id: int) -> BookOut:
    form_data = await request.form()
    payload = dict(form_data.items())

    async with httpx.AsyncClient() as client:
        response = await client.patch(
            url=request.url_for("update_book", book_id=book_id),
            json=payload)

    return BookOut(**response.json())


async def delete_book_by_id(request: Request,
                            book_id: int) -> None:
    async with httpx.AsyncClient() as client:
        await client.delete(url=request.url_for("delete_book",
                                                book_id=book_id))
