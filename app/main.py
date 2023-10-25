import os
from fastapi import FastAPI, Depends, HTTPException, status, Security
from app.config import Settings
import app.controllers.endpoint_controller as endpoint_controller
from app.config import description
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from fastapi.templating import Jinja2Templates

settings = Settings()

app = FastAPI(
    title="StreetView - API backend",
    description=description,
    version=settings.api_prefix,
)
api_prefix = settings.api_prefix

@app.on_event('startup')
async def startup_event():
    BASE_DIR = Path(__file__).resolve().parent
    templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
    #templates = Jinja2Templates(directory="templates")
    app.package = {
        "templates":templates,
    }

app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    endpoint_controller.router,
    prefix=f"/{api_prefix}/endpoint",
    tags=['endpoint'],
    # dependencies=[Security(get_current_active_user, scopes=["admin"])],
)
#app.mount("/static", StaticFiles(directory="static"), name="static")

#templates = Jinja2Templates(directory="templates")
