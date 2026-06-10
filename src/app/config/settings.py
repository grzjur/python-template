from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.paths import Paths


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    VERSION: str = "0.1.0"
    paths: Paths = Field(default_factory=Paths)


@lru_cache
def get_config() -> Config:
    return Config()


config = get_config()
