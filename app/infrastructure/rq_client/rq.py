import aio_pika
from app.config.conf import RabbitConfig
from app.utils.encoder import encode_model
from pydantic import BaseModel



class RabbitClient:
    def __init__(self, config: RabbitConfig)->None:
        self.config = config
        self.connection: aio_pika.RobustConnection | None = None
        self.channel: aio_pika.RobustChannel | None = None
        self.exchange: aio_pika.Exchange | None = None

    async def connect(self)->None:
        if self.connection:
            return
        self.connection = await aio_pika.connect_robust(host=self.config.host,
                                                  port=self.config.port,
                                                  login=self.config.login,
                                                  password=self.config.password.get_secret_value())
        self.channel = await self.connection.channel()
        self.exchange = await self.channel.declare_exchange(
            "api_router",
            aio_pika.ExchangeType.TOPIC,
            durable=True
        )

    async def publish(self, 
                      obj: BaseModel, 
                      headers: dict, 
                      routing_key: str)->None:
        if not self.exchange:
            await self.connect()
        
        payload = encode_model(obj=obj)
        message = aio_pika.Message(
            body=payload,
            headers=headers or {},
            content_type="application/json",
            delivery_mode=aio_pika.DeliveryMode.NOT_PERSISTENT
        )
        await self.exchange.publish(
            message=message,
            routing_key=routing_key,
            mandatory=False
        )
    async def close(self)->None:
        await self.connection.close()