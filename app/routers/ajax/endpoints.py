from fastapi import Depends, Request
from fastapi.responses import HTMLResponse

from . import router
from .requests import (
    create_book_with_form_data,
    delete_book_by_id,
    get_book_by_id,
    search_for_books_by,
    update_book_by_id
)
from app import templates
from app.routers.library.models import BookOut, Category


@router.get("/books/btn")
async def create_book_btn(
        request: Request
):
    return templates.TemplateResponse("open/shared/create-book-btn.html",
                                      dict(request=request))


@router.get("/books/form")
async def create_book_form(
        request: Request
):
    return templates.TemplateResponse("open/shared/create-book-form.html",
                                      dict(request=request))


@router.post("/books/form")
async def create_book_from_form(
        request: Request
):
    form_data = await request.form()
    await create_book_with_form_data(request, dict(form_data.items()))
    return templates.TemplateResponse("open/shared/create-book-btn.html",
                                      dict(request=request))


@router.get("/search")
async def search_books(
        *,
        books: list[BookOut] = Depends(search_for_books_by),
        request: Request
):
    return templates.TemplateResponse(
        "open/shared/search-results.html",
        dict(request=request, books=books))


@router.get("/books/{book_id}")
async def read_book_ajax(
        *,
        book: int = Depends(get_book_by_id),
        request: Request
):
    return templates.TemplateResponse("open/shared/get-book-row.html",
                                      dict(request=request, book=book))


@router.get("/books/edit/{book_id}")
async def get_book_edit(
        *,
        book: BookOut = Depends(get_book_by_id),
        request: Request
):
    return templates.TemplateResponse("open/shared/edit-book-form.html",
                                      dict(request=request,
                                           book=book,
                                           Category=Category))


@router.put("/books/{book_id}")
async def update_book_ajax(
        *,
        book: BookOut = Depends(update_book_by_id),
        request: Request
):
    return templates.TemplateResponse("open/shared/get-book-row.html",
                                      dict(request=request, book=book))


@router.delete("/books/{book_id}")
async def delete_book_ajax(
        book_id: int,
        request: Request
):
    await delete_book_by_id(request, book_id)
    return HTMLResponse("")
