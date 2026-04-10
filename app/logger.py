# Base
import logging
import sys

logger: logging.Logger = logging.getLogger("ROOT")


def setup_root(
    name: str,
    level: str = logging.DEBUG,
    message_format: str = "%(asctime)s %(levelname)s %(name)s %(message)s",
    datetime_format: str = "%Y-%m-%d %H:%M:%S",
):
    global logger
    root_formatter = logging.Formatter(message_format, datetime_format)
    root_handler = logging.StreamHandler(sys.stdout)
    root_handler.setFormatter(root_formatter)
    logging.root.setLevel(level)
    logging.root.handlers = [root_handler]
    logger.name = name


def getLogger(name: str) -> logging.Logger:
    return logging.getLogger(name)
