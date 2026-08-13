import time
import uuid

from backend.app.core.logger import logger
from backend.app.agents.gemini_agent import app, AgentResponse


def run_agent(message: str):

    request_id = str(uuid.uuid4())
    start_time = time.time()

    logger.info(
        f"AGENT_REQUEST_STARTED | "
        f"request_id={request_id}"
    )

    max_attempts = 3

    for attempt in range(1, max_attempts + 1):

        try:

            logger.info(
                f"AGENT_ATTEMPT_STARTED | "
                f"request_id={request_id} | "
                f"attempt={attempt}"
            )

            result = app.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": message,
                        }
                    ]
                }
            )

            duration = time.time() - start_time

            logger.info(
                f"AGENT_REQUEST_SUCCESS | "
                f"request_id={request_id} | "
                f"attempt={attempt} | "
                f"duration={duration:.2f}s"
            )

            return result["response"]

        except Exception as exc:

            duration = time.time() - start_time

            error_message = str(exc)

            logger.exception(
                f"AGENT_ATTEMPT_FAILED | "
                f"request_id={request_id} | "
                f"attempt={attempt} | "
                f"duration={duration:.2f}s | "
                f"error={error_message}"
            )

            if (
                "429" in error_message
                or "RESOURCE_EXHAUSTED" in error_message
            ):

                logger.error(
                    f"AGENT_QUOTA_EXCEEDED | "
                    f"request_id={request_id}"
                )

                return AgentResponse(
                    status="error",
                    summary="The AI service has temporarily reached its usage limit. Please try again later.",
                    action_required=True,
                )

            if attempt == max_attempts:

                logger.error(
                    f"AGENT_REQUEST_FAILED | "
                    f"request_id={request_id} | "
                    f"attempts={max_attempts}"
                )

                return AgentResponse(
                    status="error",
                    summary="The AI service is temporarily unavailable. Please try again.",
                    action_required=True,
                )

            wait_time = 2 ** (attempt - 1)

            logger.info(
                f"AGENT_RETRY_SCHEDULED | "
                f"request_id={request_id} | "
                f"attempt={attempt} | "
                f"wait={wait_time}s"
            )

            time.sleep(wait_time)