import logging
import sys

LOG_FORMAT = (
    "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] "
    "%(message)s"
)

def setup_logger(name: str = "app") -> logging.Logger:
    """Simple stdout logger with clean format."""
    loggr = logging.getLogger(name)
    loggr.setLevel(logging.INFO)

    # Remove any pre-existing handlers (useful for reloads)
    for handler in loggr.handlers[:]:
        loggr.removeHandler(handler)

    # Stream handler (stdout)
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(LOG_FORMAT, "%Y-%m-%d %H:%M:%S")
    stream_handler.setFormatter(formatter)
    loggr.addHandler(stream_handler)

    loggr.propagate = False

    loggr.info("✅ Application logger initialized")
    return loggr


logger = setup_logger()
