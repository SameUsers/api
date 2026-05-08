from .v1 import router as api_router
from fastapi import APIRouter

router = APIRouter(prefix='/api')
router.include_router(api_router)