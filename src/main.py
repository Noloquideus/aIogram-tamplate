import asyncio
from src.bot import BotManager
from src.logger import logger


async def main():
    bot_manager = BotManager()
    bot_manager.setup()
    
    try:
        logger.info('Starting bot...')
        await bot_manager.start()
    except Exception as e:
        logger.error(f'Error in bot: {e}')
    finally:
        await bot_manager.close()
        logger.info('Bot stopped')


if __name__ == "__main__":
    asyncio.run(main())
