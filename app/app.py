# Requirements
from fastapi import FastAPI
from uvicorn import run
# Support
from .settings import settings
from .logger import logger, setup_root
# Lifespan
from .lifespan import lifespan
# Base router
from .web.api.v1 import base_router_v1


def application_factory() -> FastAPI:
    """Фабрика приложения
    """
    # Настройка логирования
    setup_root(
        name="APP",
        level=settings.LOG_LEVEL,
        message_format=settings.LOG_MESSAGE_FORMAT,
        datetime_format=settings.LOG_DATETIME_FORMAT,
    )
    logger.info(
        f"Логирование установлено: Logger[{logger.name}] Level[{logger.level}]"
    )
    # Инициализация приложения
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        lifespan=lifespan
    )
    # Регистрация логирования
    app.state.logger = logger
    # Регистрация путей
    app.include_router(
        router=base_router_v1,
        prefix=settings.API_V1_BASE_ROUTER,
    )
    logger.debug(
        f"Роутер: {settings.API_V1_BASE_ROUTER} успешно зарегистрирован"
    )
    logger.info(
        f"\nПриложение инициализировано: {settings.TITLE} Version[{settings.VERSION}]"
        f"\n\t{settings.DESCRIPTION}"
        f"\n\t{settings.DEBUG}"
        f"\n\t{settings.LOG_LEVEL}"
        f"\n\t{settings.SERVER_HOST}"
        f"\n\t{settings.SERVER_PORT}"
    )
    return app


def get_app_import() -> str:
    return f"{__name__}:application_factory"


def run_app():
    run(
        app=get_app_import(),
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
        factory=settings.SERVER_FACTORY,
        workers=settings.SERVER_WORKERS,
    )
