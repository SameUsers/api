from fastapi import FastAPI
from contextlib import asynccontextmanager
from .config import get_settings
from .infrastructure.redis import RedisClient
from .api import router

@asynccontextmanager
async def lifecycle(app: FastAPI):
    settings = get_settings()

    redis_client = RedisClient(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db
    )

    app.state.redis = redis_client

    yield

    await redis_client.close()

app = FastAPI(lifespan=lifecycle)
app.include_router(router)
