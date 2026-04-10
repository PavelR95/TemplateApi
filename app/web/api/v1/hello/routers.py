# Base
# Requirements
from fastapi import APIRouter, Request
# Schemas
from . import schemas
# Endpoints
from .endpoints import Endpoints

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)


@router.get("")
async def hello(request: Request) -> schemas.BaseMessage:
    return await Endpoints.hello(request)
