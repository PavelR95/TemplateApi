# Base imports
# Requirements
from fastapi import FastAPI
# Support
from ..support import settings, getLogger, Logger


async def lifespan(app: FastAPI):
    logger: Logger = app.state.logger
    logger.debug("Запуск приложения")
    yield
    logger.debug("Завершение приложения")
