"""
"""
from fastapi.openapi.utils import get_openapi

from . import version
from .core.config import settings
from .core.database import Base, engine
from .main import create_app
from .routes import api_v1

Base.metadata.create_all(bind=engine)
app = create_app()
app.include_router(api_v1, prefix=f"{settings.API_VERSION_PREFIX}")
app.openapi_schema = get_openapi(
    title="Landlords API",
    version=version,
    description=(
        "NEXTERS 17th 건물주팀 API</br>"
        "<hr>"
        "<h3>개발자</h3>"
        "<p>[15기 박다예](https://github.com/parkdaye)</p>"
        "<p>[15기 김민철](https://github.com/mcauto)</p>"
    ),
    routes=app.routes,
)
