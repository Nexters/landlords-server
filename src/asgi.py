"""
"""
from .core.config import settings
from .main import create_app
from .routes import api_v1

app = create_app()
app.include_router(api_v1, prefix=f"{settings.API_VERSION_PREFIX}")
