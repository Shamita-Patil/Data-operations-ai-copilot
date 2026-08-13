import logging
import os
from logging.handlers import RotatingFileHandler

# ---------------------------------------
# Create Logs Directory
# ---------------------------------------

LOG_DIR = "backend/app/logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

# ---------------------------------------
# Create Logger
# ---------------------------------------

logger = logging.getLogger("data_ops_ai")

logger.setLevel(logging.INFO)
logger.propagate = False

# ---------------------------------------
# Log Format
# ---------------------------------------

formatter = logging.Formatter(
"%(asctime)s | %(levelname)s | %(name)s | %(message)s"

)

# ---------------------------------------
# File Handler
# ---------------------------------------

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

# ---------------------------------------
# Console Handler
# ---------------------------------------

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

# ---------------------------------------
# Prevent Duplicate Logs
# ---------------------------------------

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
