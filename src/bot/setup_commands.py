from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from src.bot.core.enums import Commands
from src.bot.core.lexicon import LEXICON
from src.logger import logger


async def set_commands(bot: Bot) -> None:
    logger.info("Setting up bot commands...")
    
    try:
        commands = [
            BotCommand(
                command=Commands.START.value,
                description=LEXICON['en']['cmd_start_desc']
            ),
            BotCommand(
                command=Commands.MENU.value,
                description=LEXICON['en']['cmd_menu_desc']
            )
        ]

        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeDefault()
        )
        logger.info("Bot commands have been set successfully")
    except Exception as e:
        logger.error(f"Failed to set bot commands: {e}")
        raise
