from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from src.bot.handlers import common_router
from src.bot.setup_commands import set_commands
from src.bot.storage import StorageManager
from src.bot.middlewares.i18n import I18nMiddleware
from src.bot.middlewares.trace import TraceMiddleware
from src.bot.core.session import SessionManager
from src.settings import settings
from src.logger import logger


class BotManager:
    def __init__(self):
        logger.info('Initializing bot manager...')
        self.bot = Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML,
                link_preview_is_disabled=True,
                disable_notification=False,
                protect_content=False,
                allow_sending_without_reply=True
            )
        )
        self.storage_manager = StorageManager()
        self.session_manager = SessionManager(self.storage_manager.redis_client)
        self.dp = Dispatcher(storage=self.storage_manager.storage)
        logger.info('Bot manager initialized successfully')

    def setup(self):
        logger.info('Setting up bot components...')

        self.dp.update.outer_middleware(TraceMiddleware(self.session_manager))
        self.dp.update.outer_middleware(I18nMiddleware())

        self.dp.include_router(common_router)

        logger.info('Bot components have been set up successfully')

    async def start(self):
        logger.info('Starting bot...')
        try:
            await set_commands(self.bot)
            await self.dp.start_polling(self.bot)
        except Exception as e:
            logger.error(f'Error while running bot: {e}')
            raise

    async def close(self):
        logger.info('Shutting down bot...')
        try:
            await self.storage_manager.close()
            await self.bot.session.close()
            logger.info('Bot has been shut down successfully')
        except Exception as e:
            logger.error(f'Error while shutting down bot: {e}')
            raise
