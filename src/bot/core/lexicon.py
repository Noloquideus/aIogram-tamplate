from typing import Dict


LEXICON: Dict[str, Dict[str, str]] = {
    'ru': {
        'common_message': 'Добро пожаловать! Я бот для управления базой данных.\n\nВыберите действие:',
        'button_menu': 'Меню',
        'button_help': 'Помощь',
        'cmd_start_desc': 'Запустить бота',
        'cmd_menu_desc': 'Показать главное меню',
        'cmd_about_desc': 'Информация о боте',
        'about_message': 'Я бот для управления базой данных. Я умею:\n\n• Показывать меню\n• Помогать с управлением базой данных\n• Отвечать на команды',
        'db_connected': 'База данных успешно подключена!',
        'db_disconnected': 'База данных отключена.',
        'db_list': 'Список доступных баз данных:',
        'db_connection_error': 'Ошибка подключения к базе данных.',
        'db_not_connected': 'База данных не подключена. Пожалуйста, подключите базу данных.'
    },
    'en': {
        'common_message': 'Welcome! I am a database management bot.\n\nSelect an action:',
        'button_menu': 'Menu',
        'button_help': 'Help',
        'cmd_start_desc': 'Start the bot',
        'cmd_menu_desc': 'Show main menu',
        'cmd_about_desc': 'About the bot',
        'about_message': 'I am a database management bot. I can:\n\n• Show menu\n• Help with database management\n• Respond to commands',
        'db_connected': 'Database successfully connected!',
        'db_disconnected': 'Database disconnected.',
        'db_list': 'List of available databases:',
        'db_connection_error': 'Database connection error.',
        'db_not_connected': 'Database is not connected. Please connect to a database.'
    }
}
