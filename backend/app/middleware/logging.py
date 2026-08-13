import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from backend.app.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())

        start_time = time.time()

        try:
            response = await call_next(request)

        except Exception:

            logger.exception(
                f"[{request_id}] Unhandled exception while processing request"
            )

            raise

        process_time = time.time() - start_time

        logger.info(
            f"[{request_id}] "
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{process_time:.4f}s"
        )

        return response
