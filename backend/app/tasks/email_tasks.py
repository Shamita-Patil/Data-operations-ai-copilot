import random
import time

from backend.app.core.logger import logger
from backend.app.tasks.celery_app import celery


@celery.task(
    queue="email",
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def send_welcome_email(
    email: str,
):
    logger.info(
        f"Sending welcome email to {email}"
    )

    time.sleep(2)

    # Simulate random failure
    if random.choice([True, False]):
        logger.error(
            "SMTP Server unavailable"
        )
        raise Exception("SMTP Failure")

    #logger.error(
    #    "SMTP Server unavailable"
    #)

    #raise Exception("SMTP Failure")

    logger.info(
        f"Welcome email sent to {email}"
    )
