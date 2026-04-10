# Base
# Requirements
from fastapi import APIRouter
# Routers
from .hello import router as hello_router

base_router_v1 = APIRouter()
base_router_v1.include_router(hello_router)
