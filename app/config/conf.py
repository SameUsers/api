from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class RedisConfig(BaseModel):
    port: int
    host: str
    db: int

class Config(BaseSettings):
    redis: RedisConfig

    model_config = SettingsConfigDict(
        env_nested_delimiter='__'
    )

