from fastapi import APIRouter
from .ingestor import ingestor
from .query import query

router = APIRouter(prefix='/api')

router.include_router(ingestor.router)
router.include_router(query.router)
