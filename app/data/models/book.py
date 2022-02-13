from tortoise import fields, models

from app.shared.enums import BookStatus


class BookDB(models.Model):
    id: int = fields.IntField(pk=True, generated=True)
    title: str = fields.CharField(max_length=64, null=False)
    author: str = fields.CharField(max_length=64, null=False)
    category: BookStatus = fields.CharEnumField(BookStatus, default=BookStatus.WILL_READ, max_length=10)
    book_link: str | None = fields.CharField(default=None, max_length=255)
    image_link: str | None = fields.CharField(default=None, max_length=255)

    class Meta:
        table = "books"
