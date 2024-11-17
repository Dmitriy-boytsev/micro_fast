from fastapi import FastAPI

from app.endpoints.endpoints import router as endpoints_router
from app.core.conf import settings


app = FastAPI(title=settings.app_title)
app.include_router(endpoints_router)
