from .health import router as health_router
from fastapi import APIRouter

router = APIRouter(prefix='/health', tags=['health'])
router.include_router(health_router)