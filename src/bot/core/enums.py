from enum import Enum


class Commands(str, Enum):
    START = "start"
    MENU = "menu"
    ABOUT = "about"


class CallbackData(str, Enum):
    MENU = "menu"
    HELP = "help"
    CONNECT_DB = "connect_db"
    DISCONNECT_DB = "disconnect_db"
    LIST_DB = "list_db"


class Buttons(str, Enum):
    MENU = "Меню"
    HELP = "Помощь"
    CONNECT_DB = "Подключить БД"
    DISCONNECT_DB = "Отключить БД"
    LIST_DB = "Список БД"
