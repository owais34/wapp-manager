import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from pymongo.errors import PyMongoError
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.logging_config import logger
from app.db.session import get_database
from app.utils.crud_user import create_user
from app.ws.router import websocket_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        db = get_database()
        db.list_collection_names()
        logger.info(f"✅ Connected to MongoDB: {db.name}")
    except PyMongoError as e:
        logger.critical(f"❌ Failed to connect to MongoDB: {e}")
        sys.exit(1)

    yield
    logger.info("❌ Shutting down MongoDB connection")


app = FastAPI(
    title="FastAPI Auth API",
    version="1.0.0",
    description="FastAPI authentication system using MongoDB + JWT",
    lifespan=lifespan
)

app.include_router(api_router)
app.include_router(websocket_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    try:
        create_user("admin", "password", True)
    except Exception as e:
        logger.exception("User already present")
    return {"status": "ok", "message": "FastAPI Auth API running!"}
