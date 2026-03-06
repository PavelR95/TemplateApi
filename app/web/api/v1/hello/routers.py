# Requirements
from fastapi import APIRouter, Request
# Endpoints
from .endpoints import HelloEndpoints
# Schemas
from . import schemas

router = APIRouter(
    prefix="/hello",
    tags=["hello"]
)


@router.get("/")
async def hello(request: Request) -> schemas.BaseResponse:
    return await HelloEndpoints.hello(request)
