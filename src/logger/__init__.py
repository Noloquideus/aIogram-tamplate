from src.logger.log_format import LogFormat
from src.logger.log_levels import LogLevel
from src.logger.logger import Logger

logger = Logger(min_level=LogLevel.DEBUG, log_format=LogFormat.JSON)

async def get_logger() -> Logger:
    return logger
