from fastapi import Depends, status

from . import router
from app.controllers.book import BookController, BookOut


@router.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(
        book: BookOut = Depends(BookController.create)
):
    return book


@router.get("/books", response_model=list[BookOut])
async def read_books(
        books: list[BookOut] = Depends(BookController.get_all)
):
    return books


@router.get("/books/search", response_model=list[BookOut])
async def read_books_ilike_by(
        books: list[BookOut] = Depends(BookController.get_all_ilike_by)
):
    return books


@router.get("/books/{book_id}", response_model=BookOut)
async def read_book(
        book: BookOut = Depends(BookController.get_by_id)
):
    return book


@router.patch("/books/{book_id}", response_model=BookOut,
              status_code=status.HTTP_202_ACCEPTED)
async def update_book(
        book: BookOut = Depends(BookController.update_book)
):
    return book


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
        book_id: int
):
    await BookController.delete_book(book_id)
