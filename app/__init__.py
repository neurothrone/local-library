from pathlib import Path

import fastapi_jinja
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import ConfigType, settings
from .data.db import init_db

BASE_PATH = Path(__file__).resolve().parent
template_folder = str(BASE_PATH / "templates")
templates = Jinja2Templates(directory=template_folder)


def create_app(config_type: ConfigType | None = None) -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE,
                  version=settings.PROJECT_VERSION)

    configure(app)
    register_events(app, config_type)
    register_routers(app)

    return app


def configure(app: FastAPI) -> None:
    fastapi_jinja.global_init(template_folder, auto_reload=True)
    app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")


def register_events(app: FastAPI, config_type: ConfigType | None = None) -> None:
    @app.on_event("startup")
    async def on_startup():
        await init_db(app, settings.get_db_url(config_type))

        if settings.DEBUG:
            print(settings)


def register_routers(app: FastAPI) -> None:
    from .routers.ajax import router as ajax_router
    from .routers.library import router as library_router
    from .routers.open import router as open_router

    app.include_router(ajax_router, prefix="/ajax", tags=["ajax"])
    app.include_router(library_router, tags=["library"])
    app.include_router(open_router, tags=["open"])
