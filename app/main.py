from fastapi import FastAPI

from app.endpoints.endpoints import router as endpoints_router


app = FastAPI(title="Микросервис")
app.include_router(endpoints_router)
