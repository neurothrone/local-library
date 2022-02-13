import logging
from enum import Enum

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class ConfigType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


class Settings(BaseSettings):
    DEBUG: bool = False
    PROJECT_TITLE: str = "Book Library Web App / API"
    PROJECT_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


def get_db_url(config_type: ConfigType) -> str:
    match config_type:
        case ConfigType.DEVELOPMENT:
            return "sqlite://data-dev.db"
        case ConfigType.TESTING:
            return "sqlite://:memory:"
        case _:
            return "sqlite://data.db"
