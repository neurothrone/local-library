from tortoise import fields, models

from app.shared.enums import Category


class BookDB(models.Model):
    id: int = fields.IntField(pk=True, generated=True)
    title: str = fields.CharField(max_length=64, null=False)
    author: str = fields.CharField(max_length=64, null=False)
    category: Category = fields.CharEnumField(Category,
                                              default=Category.WILL_READ,
                                              max_length=10)

    class Meta:
        table = "books"
