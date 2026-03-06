# Логирование приложения
from sys import stdout
import logging
from .settings import settings

DEFAULT_MESSAGE_FORMAT: str = "%(asctime)s %(name)s %(levelname)s %(message)s"
DEFAULT_DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
DEFAULT_LEVEL: str = "DEBUG"


try:
    from .settings import settings
    message_format: str = settings.log_message_format
    datetime_format: str = settings.log_datetime_format
    level: int = logging._nameToLevel.get(settings.log_level)
except:
    message_format: str = DEFAULT_MESSAGE_FORMAT
    datetime_format: str = DEFAULT_DATETIME_FORMAT
    level: int = logging._nameToLevel.get(DEFAULT_LEVEL)

logging.root = logging.RootLogger(level=level)
root_formatter = logging.Formatter(
    fmt=message_format,
    datefmt=datetime_format,
)
root_handler = logging.StreamHandler(stream=stdout)
root_handler.formatter = root_formatter
logging.root.addHandler(root_handler)


def getLogger(name: str) -> logging.Logger:
    logger = logging.root.manager.getLogger(name)
    logger.handlers = logging.root.handlers
    logger.setLevel(logging.root.level)
    return logger


logger = getLogger("MAIN")


def getChild(name: str) -> logging.Logger:
    child = logger.getChild(name)
    return child
