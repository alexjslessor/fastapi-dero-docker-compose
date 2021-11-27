from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.v1.dero_daemon import read_routes
from .config.config import get_settings
from .config.route_prefix import *


settings = get_settings()

SECRET = settings.SECRET
CORS_ORIGINS = settings.CORS_ORIGINS

app = FastAPI(
    openapi_url=settings.OPENAPI_URL,
    docs_url=settings.DOCS_URL, 
    redoc_url=settings.REDOC_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(read_routes.router, tags=CRUD_READ)

@app.on_event("startup")
async def startup_event():
    print('Application Startup....')


@app.on_event("shutdown")
def shutdown_event():
    print('Application Shutdown....')