from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: str
    message: str


class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Any


class FailureResponse(BaseModel):
    success: bool = False
    error: ErrorResponse
