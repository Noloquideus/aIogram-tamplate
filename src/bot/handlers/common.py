from aiogram import Router, types
from aiogram.filters import Command
from src.bot.core.enums import Commands
from src.bot.core.lexicon import LEXICON
from src.bot.keyboards.database import get_database_keyboard
from src.logger import logger

router = Router()

@router.message(Command(Commands.START.value, Commands.MENU.value))
async def handle_start_menu(
    message: types.Message,
    i18n_lang: str,
    trace_id: str,
    user_id: int
) -> None:
    chat_id = message.chat.id
    command = message.text.split()[0][1:]
    lang = i18n_lang if i18n_lang in LEXICON else 'en'

    logger.info(
        message=f'User triggered {command} command',
        trace_id=trace_id,
        user_id=str(user_id)
    )

    await message.answer(
        text=LEXICON[lang]['common_message'],
        reply_markup=get_database_keyboard(lang)
    )

    logger.info(
        message='Sent {command} command response',
        trace_id=trace_id,
        user_id=str(user_id)
    )
