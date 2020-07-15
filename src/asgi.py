"""
"""
from .core.config import settings
from .core.database import Base, engine
from .main import create_app
from .routes import api_v1

Base.metadata.create_all(bind=engine)
app = create_app()
app.include_router(api_v1, prefix=f"{settings.API_VERSION_PREFIX}")
