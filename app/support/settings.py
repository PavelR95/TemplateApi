from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Base settings
    DEBUG: bool = True
    TITLE: str = "TemplateAPI"
    DESCRIPTION: str = "TemplateAPI"
    VERSION: str = "v0.0.1"

    # Logger settings
    log_level_default: str = "INFO"
    log_message_format: str = "%(asctime)s - %(name)s [%(levelname)s] - %(message)s"
    log_datetime_format: str = "%Y-%m-%d %H:%M:%S"

    @property
    def log_level(self) -> str:
        if self.DEBUG is True:
            return "DEBUG"
        return self.log_level_default

    # App settings
    app_base_router: str = "/api/v1/template"

    # Server settings
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    server_reload: bool = True
    server_factory: bool = True
    server_workers_default: int = 1

    @property
    def server_workers(self):
        if self.server_reload is True:
            return 1
        else:
            return self.server_workers_default

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()
