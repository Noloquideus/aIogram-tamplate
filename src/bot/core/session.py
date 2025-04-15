import uuid
from datetime import datetime, timedelta, UTC
from typing import Optional
import json
from redis.asyncio import Redis


class UserSession:
    def __init__(self, trace_id: str, last_activity: datetime):
        self.trace_id = trace_id
        self.last_activity = last_activity

    @classmethod
    def create(cls) -> 'UserSession':
        return cls(
            trace_id=str(uuid.uuid4()),
            last_activity=datetime.now(UTC)
        )

    def to_json(self) -> str:
        return json.dumps({
            'trace_id': self.trace_id,
            'last_activity': self.last_activity.isoformat()
        })

    @classmethod
    def from_json(cls, data: str) -> 'UserSession':
        parsed = json.loads(data)
        return cls(
            trace_id=parsed['trace_id'],
            last_activity=datetime.fromisoformat(parsed['last_activity'])
        )


class SessionManager:
    def __init__(self, redis: Redis, session_ttl: int = 300):
        self.redis = redis
        self.session_ttl = session_ttl

    @staticmethod
    def _get_key(user_id: int) -> str:
        return f'user_session:{user_id}'

    async def get_session(self, user_id: int) -> Optional[UserSession]:
        data = await self.redis.get(self._get_key(user_id))
        if not data:
            return None
        return UserSession.from_json(data)

    async def create_or_update_session(self, user_id: int) -> UserSession:
        session = await self.get_session(user_id)

        if session:
            now = datetime.now(UTC)
            if now - session.last_activity < timedelta(seconds=self.session_ttl):
                session.last_activity = now
                await self.redis.setex(
                    self._get_key(user_id),
                    self.session_ttl,
                    session.to_json()
                )
                return session

        session = UserSession.create()
        await self.redis.setex(
            self._get_key(user_id),
            self.session_ttl,
            session.to_json()
        )
        return session
