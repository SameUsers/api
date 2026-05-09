from fastapi import APIRouter
import socket
from app.schemas import HealthSchema
router = APIRouter()

@router.get('/')
async def health()->HealthSchema:
    return HealthSchema(responsing_host=socket.gethostname())