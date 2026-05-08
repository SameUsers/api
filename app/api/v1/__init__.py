from .routes import router as v1_routes
from fastapi import APIRouter

router = APIRouter(prefix='/v1')
router.include_router(v1_routes)