from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.bot.core.enums import CallbackData
from src.bot.core.lexicon import LEXICON


def get_main_keyboard(lang: str = 'ru') -> InlineKeyboardMarkup:
    menu_button = InlineKeyboardButton(
        text=LEXICON[lang]['button_menu'],
        callback_data=CallbackData.MENU.value
    )

    help_button = InlineKeyboardButton(
        text=LEXICON[lang]['button_help'],
        callback_data=CallbackData.HELP.value
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[menu_button], [help_button]])

    return keyboard
