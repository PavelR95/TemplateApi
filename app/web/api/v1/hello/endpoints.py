# Base imports
from logging import Logger
# Requirements
from fastapi import Request
# Schemas
from . import schemas


class HelloEndpoints:

    ACCESS_NAME = "hello"

    @classmethod
    async def hello(cls, request: Request) -> schemas.BaseResponse:
        logger: Logger = request.app.state.logger
        # Endpoint code
        logger.info("Hello world!")
        # -------------
        return schemas.BaseResponse()
