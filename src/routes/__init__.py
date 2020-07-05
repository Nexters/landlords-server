"""
routes
"""
from fastapi.routing import APIRouter

from .health import health as health_router

api_v1 = APIRouter()

api_v1.include_router(health_router, prefix="/health", tags=["manage"])
