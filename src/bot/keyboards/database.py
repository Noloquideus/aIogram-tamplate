from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.bot.core.enums import CallbackData, Buttons
from src.bot.core.lexicon import LEXICON


def get_database_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text=Buttons.CONNECT_DB.value,
                callback_data=CallbackData.CONNECT_DB.value
            )
        ],
        [
            InlineKeyboardButton(
                text=Buttons.DISCONNECT_DB.value,
                callback_data=CallbackData.DISCONNECT_DB.value
            )
        ],
        [
            InlineKeyboardButton(
                text=Buttons.LIST_DB.value,
                callback_data=CallbackData.LIST_DB.value
            )
        ],
        [
            InlineKeyboardButton(
                text=Buttons.MENU.value,
                callback_data=CallbackData.MENU.value
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard) 