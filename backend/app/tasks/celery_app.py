import os

from celery import Celery
from kombu import Queue

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://localhost:6379/0",
)

celery = Celery(
    "data_ops_ai",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=False,
    task_default_queue="default",
    task_queues=(
        Queue("default"),
        Queue("email"),
        Queue("reports"),
        Queue("ai"),
    ),
)

#celery.autodiscover_tasks(
 #   ["backend.app.tasks"]
#)

from backend.app.tasks import email_tasks