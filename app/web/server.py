# Base imports
# Requirements
import uvicorn
# Application
from .app import get_app_import
# Support
from ..support import settings, logger


def run_server():
    logger.info(
        f"\n\n---- {settings.TITLE.upper()} ----\n"
        f"HOST [{settings.server_host}] PORT: [{settings.server_port}]\n"
        f"WORKERS [{settings.server_workers}]\n"
    )
    uvicorn.run(
        app=get_app_import(),
        factory=settings.server_factory,
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.server_reload,
        workers=settings.server_workers,
    )
