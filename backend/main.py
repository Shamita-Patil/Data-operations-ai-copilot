from fastapi import FastAPI

from backend.app.api.v1.router import api_router
from backend.app.core.config import settings
from backend.app.core.lifespan import lifespan
from backend.app.middleware.request_id import RequestIDMiddleware
from backend.app.middleware.logging import LoggingMiddleware
from backend.app.core.exception_handlers import register_exception_handlers
from fastapi.staticfiles import StaticFiles




app = FastAPI(
    title="Enterprise Data Operations AI API",
    description="""
## Enterprise Data Operations AI Backend

A production-ready backend built with FastAPI.

### Features

- JWT Authentication
- Role-Based Authorization
- User Management
- Address Management
- SQLAlchemy ORM
- Alembic Database Migrations
- PostgreSQL Integration
- Search
- Filtering
- Sorting
- Pagination
- One-to-Many Relationships
- JOIN Queries
- Eager Loading (joinedload)
- Request Logging
- Global Exception Handling
- Request Correlation IDs
- OpenAPI Documentation

This project follows enterprise backend development practices.
""",
    version=settings.api_version,
    debug=settings.debug,
    lifespan=lifespan,

    contact={
        "name": "Shamita Patil",
        "email": "shamita@gmail.com",
    },

    license_info={
        "name": "MIT License",
    },

    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------
# Register Global Exception Handlers
# ---------------------------------------------------------

register_exception_handlers(app)

# ---------------------------------------------------------
# Middlewares
# ---------------------------------------------------------

app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

# ---------------------------------------------------------
# API Routes
# ---------------------------------------------------------
app.mount(
    "/uploads",
    StaticFiles(directory="backend/uploads"),
    name="uploads",
)

app.include_router(
    api_router,
    prefix=f"/api/{settings.api_version}",
)


@app.get("/")
def root():
    return {
        "message": "API is running"
    }