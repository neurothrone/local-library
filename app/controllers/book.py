from fastapi import HTTPException, status, Query
from tortoise.exceptions import DoesNotExist

from app.data.models.book import BookDB
from app.data.repository.book import BookRepository
from app.routers.library.models import BookIn, BookOut, BookUpdate


class BookController:
    # region Utility

    @classmethod
    async def _get_book_or_404(cls,
                               book_id: int
                               ) -> BookDB:
        try:
            return await BookRepository.get_by_id_or_exc(book_id)
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Book not found.")

    # endregion Utility

    # region CRUD

    @classmethod
    async def create(cls, book: BookIn) -> BookOut:
        book_db = await BookRepository.create(**book.dict())
        return BookOut.from_orm(book_db)

    @classmethod
    async def get_all(cls,
                      offset: int = 0,
                      limit: int = Query(default=100, lte=100)
                      ) -> list[BookOut]:
        books_db = await BookRepository.get_all(offset, limit)
        return [BookOut.from_orm(book) for book in books_db]

    @classmethod
    async def get_by_id(cls,
                        book_id: int
                        ) -> BookOut:
        book_db = await cls._get_book_or_404(book_id)
        return BookOut.from_orm(book_db)

    @classmethod
    async def update_book(cls,
                          book_id: int,
                          book_update: BookUpdate
                          ) -> BookOut:
        book_db = await BookController._get_book_or_404(book_id)
        updated_book_db = await BookRepository.update_book(
            book_db, book_update.dict(exclude_unset=True))
        return BookOut.from_orm(updated_book_db)

    @classmethod
    async def delete_book(cls,
                          book_id: int
                          ) -> None:
        book_db = await BookController._get_book_or_404(book_id)
        await BookRepository.delete_book(book_db)

    # endregion CRUD
