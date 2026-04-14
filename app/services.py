# Base
from logging import Logger, getLogger
# Requirements
# Services
from . import _services as services
# Support
from .settings import settings


class Services:

    def __init__(self, logger: Logger = None):
        self.logger = logger or getLogger(__name__)

    def setup(self):
        """Инициализация и установка сервисов приложения
        """
        self.logger.debug(
            "Инициализация и установка сервисов приложения"
        )

    async def startup(self):
        """Запуск фоновых процессов и служб сервисов
        """
        self.logger.debug(
            "Запуск фоновых процессов и служб сервисов"
        )

    async def shutdown(self):
        """Остановка фоновых процессов и служб сервисов
        """
        self.logger.debug(
            "Остановка фоновых процессов и служб сервисов"
        )
