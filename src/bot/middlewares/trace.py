from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from src.bot.core.session import SessionManager
from src.logger import logger
from datetime import datetime, UTC


class TraceMiddleware(BaseMiddleware):
    def __init__(self, session_manager: SessionManager):
        self.session_manager = session_manager
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data.get('event_from_user', None)
        if not isinstance(user, User):
            logger.warning('No user found in event data')
            return await handler(event, data)

        session = await self.session_manager.create_or_update_session(user.id)

        if session.last_activity == datetime.now(UTC):
            logger.info(
                'New session created',
                trace_id=session.trace_id,
                user_id=str(user.id)
            )
        else:
            logger.info(
                'Existing session updated',
                trace_id=session.trace_id,
                user_id=str(user.id)
            )

        data['trace_id'] = session.trace_id
        data['user_id'] = user.id

        try:
            return await handler(event, data)
        except Exception as e:
            logger.error(
                message=f'Error processing request: {str(e)}',
                trace_id=session.trace_id,
                user_id=str(user.id),
            )
            raise
