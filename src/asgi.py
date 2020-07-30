"""
"""
from fastapi.openapi.utils import get_openapi
from starlette.middleware.sessions import SessionMiddleware

from . import version
from .apps.oauth.client import oauth_client
from .apps.oauth.routes import router as well_known_router
from .core.config import settings
from .core.database import Base, engine
from .main import create_app
from .routes import api_v1

Base.metadata.create_all(bind=engine)
app = create_app()
app.include_router(api_v1, prefix=f"{settings.API_VERSION_PREFIX}")
app.include_router(well_known_router, prefix="/.well-known", tags=["auth"])

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.mount(path="/oauth", app=oauth_client, name="oauth")

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
