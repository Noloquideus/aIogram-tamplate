import redis.asyncio as redis
from aiogram.fsm.storage.redis import RedisStorage
from src.settings import settings


class StorageManager:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.KEYDB_HOST,
            port=settings.KEYDB_PORT,
            db=0,
            decode_responses=True
        )
        self.storage = RedisStorage(redis=self.redis_client)

    async def close(self):
        await self.redis_client.close()
