from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from backend.app.core.logger import logger


async def global_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """
    Global exception handler.

    This catches all unhandled exceptions in the application,
    logs the complete traceback, and returns a standardized
    JSON response.
    """

    logger.exception(
        f"Unhandled Exception | "
        f"Method={request.method} | "
        f"Path={request.url.path} | "
        f"Error={str(exc)}"
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False,
            "error": {
                "code": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred."
            }
        },
    )
