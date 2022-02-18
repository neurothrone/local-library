from pydantic import BaseModel, Field

from app.shared.enums import Category


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    category: Category = Field(default=Category.WILL_READ,
                               title="User status with this book")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "Dune",
                "author": "Frank Herbert",
                "category": Category.HAVE_READ
            }
        }


class BookIn(BookBase):
    pass


class BookUpdate(BookBase):
    title: str | None = Field(default=None, min_length=1, max_length=50)
    author: str | None = Field(default=None, min_length=1, max_length=50)
    category: Category | None = Field(default=None,
                                      title="User status with this book")


class BookOut(BookBase):
    id: int
