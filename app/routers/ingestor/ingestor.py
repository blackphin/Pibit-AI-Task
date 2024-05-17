# FastAPI Imports
from fastapi import APIRouter, Depends, HTTPException, Request, Security, status

# Schema Imports
from routers.ingestor import schemas

# Services Imports
from routers.ingestor import services

router = APIRouter(tags=['Error Ingestor'], prefix='/ingestor')

# Health Check


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Ingestor Active"}


@router.post("/error/{api_name}", status_code=status.HTTP_201_CREATED)
def error_ingestor(api_name: str, payload: schemas.IngestorSchema):
    try:
        services.log_error(api_name, payload.message, payload.level)
        return {"status": "Error Ingested!"}
    except Exception as e:
        return {"status": e}
