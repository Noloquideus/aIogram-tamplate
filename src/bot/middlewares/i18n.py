from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from src.logger import logger


class I18nMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data.get('event_from_user', None)
        trace_id = data.get('trace_id', 'N/A')
        user_id = data.get('user_id', 'N/A')

        if not isinstance(user, User):
            logger.debug(
                "No user found in event, using default language: en",
                trace_id=trace_id,
                user_id=user_id
            )
            data['i18n_lang'] = 'en'
            return await handler(event, data)

        raw_lang = user.language_code or 'en'
        lang = raw_lang.split('-')[0].lower()
        logger.debug(
            f"User {user.id} raw language: {raw_lang}, processed language: {lang}",
            trace_id=trace_id,
            user_id=str(user.id)
        )

        if lang not in ['ru', 'en']:
            lang = 'en'
            logger.debug(
                f"Language {lang} not supported, using English for user {user.id}",
                trace_id=trace_id,
                user_id=str(user.id)
            )

        data['i18n_lang'] = lang
        return await handler(event, data)
