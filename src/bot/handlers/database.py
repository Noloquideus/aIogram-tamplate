from aiogram import Router, types
from src.bot.core.enums import CallbackData
from src.bot.core.lexicon import LEXICON
from src.bot.keyboards.database import get_database_keyboard
from src.logger import logger

router = Router()

@router.callback_query(lambda c: c.data == CallbackData.CONNECT_DB.value)
async def handle_connect_db(callback: types.CallbackQuery, i18n_lang: str) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    lang = i18n_lang if i18n_lang in LEXICON else 'en'
    
    logger.info(
        "User requested database connection",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "connect_db"
        }
    )
    
    # Здесь будет логика подключения к базе данных
    # Пока просто показываем сообщение
    await callback.message.edit_text(
        text=LEXICON[lang]['db_connected'],
        reply_markup=get_database_keyboard(lang)
    )
    
    logger.info(
        "Database connection message sent",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "connect_db_response"
        }
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == CallbackData.DISCONNECT_DB.value)
async def handle_disconnect_db(callback: types.CallbackQuery, i18n_lang: str) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    lang = i18n_lang if i18n_lang in LEXICON else 'en'
    
    logger.info(
        "User requested database disconnection",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "disconnect_db"
        }
    )
    
    # Здесь будет логика отключения от базы данных
    # Пока просто показываем сообщение
    await callback.message.edit_text(
        text=LEXICON[lang]['db_disconnected'],
        reply_markup=get_database_keyboard(lang)
    )
    
    logger.info(
        "Database disconnection message sent",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "disconnect_db_response"
        }
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == CallbackData.LIST_DB.value)
async def handle_list_db(callback: types.CallbackQuery, i18n_lang: str) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    lang = i18n_lang if i18n_lang in LEXICON else 'en'
    
    logger.info(
        "User requested database list",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "list_db"
        }
    )
    
    # Здесь будет логика получения списка баз данных
    # Пока просто показываем сообщение
    await callback.message.edit_text(
        text=LEXICON[lang]['db_list'],
        reply_markup=get_database_keyboard(lang)
    )
    
    logger.info(
        "Database list message sent",
        extra={
            "user_id": str(user_id),
            "chat_id": str(chat_id),
            "language": lang,
            "action": "list_db_response"
        }
    )
    await callback.answer() 