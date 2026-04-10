# Base
from logging import Logger
# Requirements
from fastapi import Request
# Services
from .....services import Services
# Schemas
from . import schemas


class Endpoints:

    endpoints: str = "Hello"

    @classmethod
    async def hello(cls, request: Request) -> schemas.BaseMessage:
        services: Services = request.app.state.services
        logger: Logger = request.app.state.logger
        logger.debug(
            f"Endpoints[{cls.endpoints}]"
        )
        return schemas.BaseMessage()
