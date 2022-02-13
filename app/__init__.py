from pathlib import Path

import fastapi_jinja
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import ConfigType, get_db_url, settings
from .data.db import init_db
from .routers.library import router as library_router
from .routers.open import router as open_router

BASE_PATH = Path(__file__).resolve().parent
template_folder = str(BASE_PATH / "templates")
templates = Jinja2Templates(directory=template_folder)


def create_app(config_type: ConfigType = ConfigType.DEVELOPMENT) -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_TITLE,
                   version=settings.PROJECT_VERSION)

    configure(_app)
    register_events(_app, config_type)
    register_routers(_app)

    return _app


def configure(_app: FastAPI) -> None:
    fastapi_jinja.global_init(template_folder, auto_reload=True)
    _app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")


def register_events(_app: FastAPI, config_type: ConfigType) -> None:
    @_app.on_event("startup")
    async def on_startup():
        await init_db(_app, get_db_url(config_type))

        if settings.DEBUG:
            print(settings)


def register_routers(_app: FastAPI) -> None:
    _app.include_router(library_router, tags=["library"])
    _app.include_router(open_router, tags=["open"])
