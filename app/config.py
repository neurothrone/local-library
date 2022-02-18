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
    PROJECT_TITLE: str = "Local Library Web App / API"
    PROJECT_VERSION: str = "1.0.0"

    DB_URL: str | None = None
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = True

    def get_db_url(self, config_type: ConfigType | None = None) -> str:
        if not config_type:
            config_type = ConfigType(self.ENVIRONMENT)

        if self.DB_URL and config_type == ConfigType.PRODUCTION:
            return self.DB_URL

        match config_type:
            case ConfigType.DEVELOPMENT:
                return "sqlite://data-dev.db"
            case ConfigType.TESTING:
                return "sqlite://:memory:"
            case _:
                return "sqlite://data.db"


settings = Settings()
