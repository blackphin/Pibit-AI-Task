# FastAPI Imports
from fastapi import APIRouter, Depends, HTTPException, Request, Security, status

# Schema Imports
from routers.query import schemas

# Services Imports
from routers.query import services

router = APIRouter(tags=['Query Interface'], prefix='/query')

# Health Check


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Query Interface Active"}
