from app.data.models.book import BookDB


class BookRepository:
    @classmethod
    async def create(cls, **kwargs) -> BookDB:
        return await BookDB.create(**kwargs)

    @classmethod
    async def get_by_id_or_exc(cls,
                               book_id: int
                               ) -> BookDB:
        return await BookDB.get(id=book_id)

    @classmethod
    async def get_all(cls,
                      offset: int,
                      limit: int
                      ) -> list[BookDB]:
        return await BookDB.all().offset(offset).limit(limit)

    @classmethod
    async def update_book(cls,
                          book_db: BookDB,
                          new_data: dict
                          ) -> BookDB:
        await book_db.update_from_dict(new_data)
        await book_db.save()
        return book_db

    @classmethod
    async def delete_book(cls,
                          book_db: BookDB
                          ) -> None:
        await book_db.delete()
