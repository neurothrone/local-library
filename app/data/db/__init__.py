from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


async def init_db(app: FastAPI, db_url: str) -> None:
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.data.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
