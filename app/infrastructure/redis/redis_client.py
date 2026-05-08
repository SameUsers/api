import redis.asyncio as redis


class RedisClient:
    def __init__(self, host: str, port: int, db: int = 0):
        self._client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    @property
    def client(self) -> redis.Redis:
        return self._client

    async def close(self) -> None:
        await self._client.connection_pool.disconnect()