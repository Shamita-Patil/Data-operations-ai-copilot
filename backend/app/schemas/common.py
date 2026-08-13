from datetime import datetime

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class ApiResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None
    timestamp: datetime
