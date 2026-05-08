from pydantic import BaseModel, Field
from datetime import datetime
from app.utils import get_time

class HealthSchema(BaseModel):
    responsing_host: str
    time: datetime = Field(default_factory=get_time, alias='utcTime')