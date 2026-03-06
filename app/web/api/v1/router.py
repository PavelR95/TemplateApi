import os
# Requirements
from fastapi import APIRouter
# Routers
from .hello.routers import router as hello_router

router_v1 = APIRouter(
    tags=["v1"]
)
router_v1.include_router(hello_router)
