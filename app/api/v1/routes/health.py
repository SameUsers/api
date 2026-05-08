from fastapi import APIRouter
from app.schemas import HealthSchema

router = APIRouter()

@router.get('/')
def health()->HealthSchema:
    return HealthSchema()