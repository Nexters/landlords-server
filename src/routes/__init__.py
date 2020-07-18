"""
routes
"""
from fastapi.routing import APIRouter

from ..apps.rooms.routes import router as room_router
from .health import health as health_router

api_v1 = APIRouter()

api_v1.include_router(health_router, prefix="/health", tags=["manage"])
api_v1.include_router(room_router, prefix="/rooms", tags=["rooms"])
