from src.bot.handlers.common import router as common_router
from src.bot.handlers.database import router as database_router

routers = [common_router, database_router]

__all__ = ['common_router', 'database_router', 'routers']
