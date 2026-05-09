from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, SecretStr


class RedisConfig(BaseModel):
    port: int
    host: str
    db: int

class RabbitConfig(BaseModel):
    port: int
    host: str
    login: str
    password: SecretStr

class Config(BaseSettings):
    redis: RedisConfig
    rabbit: RabbitConfig

    model_config = SettingsConfigDict(
        env_nested_delimiter='__'
    )

