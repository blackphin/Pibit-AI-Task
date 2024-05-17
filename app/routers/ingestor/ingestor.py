# FastAPI Imports
from fastapi import APIRouter, Depends, HTTPException, Request, Security, status

# Schema Imports
from routers.ingestor import schemas

# Services Imports
from routers.ingestor import services as ingestor_services
from routers.query import services as query_services

router = APIRouter(tags=['Error Ingestor'], prefix='/ingestor')

# Health Check


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Ingestor Active"}


@router.post("/error/{api_name}", status_code=status.HTTP_201_CREATED)
def error_ingestor(api_name: str, payload: schemas.IngestorSchema):
    try:
        ingestor_services.log_error(api_name, payload.message, payload.level)
        query_services.update_error_log(
            ingestor_services.get_log_path(api_name) + ".log")
        return {"status": "Error Ingested!"}
    except Exception as e:
        return {"status": e}
