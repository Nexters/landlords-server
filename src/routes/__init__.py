"""
routes
"""
from fastapi.routing import APIRouter

from ..apps.checklist.routes import router as checklist_router
from ..apps.persona.routes import router as persona_router
from ..apps.rooms.routes import router as room_router
from .health import health as health_router

api_v1 = APIRouter()

api_v1.include_router(health_router, prefix="/health", tags=["manage"])
api_v1.include_router(room_router, prefix="/rooms", tags=["rooms"])
api_v1.include_router(persona_router, prefix="/persona", tags=["persona"])
api_v1.include_router(checklist_router, prefix="/checklist", tags=["checklist"])
