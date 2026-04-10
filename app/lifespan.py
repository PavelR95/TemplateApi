# Base
# Requirements
from fastapi import FastAPI
# Services
from .services import Services


async def lifespan(app: FastAPI):
    """Жизненный цикл приложения"""
    # Инициализация сервисов
    services = Services()
    services.setup()
    # Регистрация сервисов в приложении
    app.state.services = services
    # Запуск сервисов
    await services.startup()
    yield
    # Остановка сервисов
    await services.shutdown()
