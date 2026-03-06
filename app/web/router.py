# Requirements
from fastapi import APIRouter
# Support
from ..support import settings
# Routers
from .api.v1 import router_v1

base_router = APIRouter(
    prefix=settings.app_base_router,
    tags=["base_router"]
)
base_router.include_router(
    router_v1,
)
