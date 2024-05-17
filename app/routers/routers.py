from fastapi import APIRouter
from .ingestor import ingestor

router = APIRouter(prefix='/api')

router.include_router(ingestor.router)
