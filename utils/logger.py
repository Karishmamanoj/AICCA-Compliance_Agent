import logging
import uuid
import json
from pathlib import Path

# Where logs will be stored
LOG_TEXT = Path("logs/aicca.log")
LOG_JSON = Path("logs/aicca.jsonl")

# Ensure folder exists
LOG_TEXT.parent.mkdir(parents=True, exist_ok=True)


def new_trace_id():
    """Generate unique ID per audit run"""
    return str(uuid.uuid4())


def get_logger(name="AICCA"):
    """Create a logger that prints to console + file."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if re-run
    if logger.handlers:
        return logger

    # Format for console + file
    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(trace_id)s | %(component)s | %(message)s"
    )

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler(LOG_TEXT, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger


def json_log(trace_id, component, level, message, extra=None):
    """Write logs to JSON lines file."""
    entry = {
        "ts": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "trace_id": trace_id,
        "component": component,
        "level": level,
        "message": message,
        "extra": extra or {}
    }
    with open(LOG_JSON, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
