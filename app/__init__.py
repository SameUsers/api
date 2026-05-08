from fastapi import FastAPI
from contextlib import asynccontextmanager
from .api import router

@asynccontextmanager
async def lifecycle(app: FastAPI):
    app.include_router(router)
    yield

app = FastAPI(lifespan=lifecycle)