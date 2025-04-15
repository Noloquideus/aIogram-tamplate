from typing import List
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv('.env'))


class Settings(BaseSettings):
    PYTHONPATH: str
    BOT_TOKEN: str
    ADMINS_IDS: str

    KEYDB_HOST: str
    KEYDB_PORT: int
    DATA_TTL: int
    STATE_TTL: int

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def ADMINS(self) -> List[int]:
        return [int(x) for x in self.ADMINS_IDS.split(',')]

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', enable_decoding=True)


settings = Settings()

