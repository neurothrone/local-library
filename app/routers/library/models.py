from pydantic import BaseModel, Field, HttpUrl

from app.shared.enums import BookStatus


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    category: BookStatus = Field(default=BookStatus.WILL_READ, title="User status with this book")
    book_link: HttpUrl | None = None
    image_link: HttpUrl | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "Dune",
                "author": "Frank Herbert",
                "category": BookStatus.HAVE_READ,
                "book_link": "https://www.goodreads.com/book/show/44767458-dune",
                "image_link": "https://i.gr-assets.com/images/S/compressed.photo.goodreads"
                              ".com/books/1555447414l/44767458.jpg"
            }
        }


class BookIn(BookBase):
    book_link: HttpUrl | None = None
    image_link: HttpUrl | None = None


class BookUpdate(BookBase):
    title: str | None = Field(default=None, min_length=1, max_length=50)
    author: str | None = Field(default=None, min_length=1, max_length=50)
    category: BookStatus | None = Field(default=None, title="User status with this book")


class BookOut(BookBase):
    id: int
