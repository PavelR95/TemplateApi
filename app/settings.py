# Base
# Requirements
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Common settings
    DEBUG: bool = True
    TITLE: str = "Application"
    DESCRIPTION: str = "FastAPI and Uvicorn APP-SERVER"
    VERSION: str = "v0.0.1"

    # Logger settings
    LOG_LEVEL_DEFAULT: str = "INFO"
    LOG_MESSAGE_FORMAT: str = "%(asctime)s - %(name)s [%(levelname)s] - %(message)s"
    LOG_DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    @property
    def LOG_LEVEL(self) -> str:
        if self.DEBUG is True:
            return "DEBUG"
        return self.LOG_LEVEL_DEFAULT

    # Server settings
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_RELOAD: bool = True
    SERVER_FACTORY: bool = True
    SERVER_WORKERS_DEFAULT: int = 1

    # API settings
    API_V1_BASE_ROUTER: str = "/api/v1/application"

    @property
    def SERVER_WORKERS(self):
        if self.SERVER_RELOAD is True:
            return 1
        return self.SERVER_WORKERS_DEFAULT

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()
