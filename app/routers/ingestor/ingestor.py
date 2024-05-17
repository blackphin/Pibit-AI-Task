# FastAPI Imports
from fastapi import APIRouter, Depends, HTTPException, Request, Security, status

router = APIRouter(tags=['Error Ingestor'], prefix='/ingestor')

# Health Check


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Ingestor Active"}
