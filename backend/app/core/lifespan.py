from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.core.database import create_tables
from backend.app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Application Starting...")

    create_tables()

    yield

    logger.info("Application Stopping...")
