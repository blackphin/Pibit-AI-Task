# System Imports
from datetime import datetime
from typing import Annotated, Optional

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


@router.get("/search", status_code=status.HTTP_200_OK)
def search_logs(
    start_timestamp: Optional[datetime] = None,
    end_timestamp: Optional[datetime] = datetime.now(),
    level: Optional[str] = None,
    log_string: Optional[str] = "level",
    source: Optional[str] = None,
):
    if (start_timestamp is not None) and (end_timestamp is not None) and (start_timestamp > end_timestamp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start timestamp cannot be greater than end timestamp"
        )

    collection = services.get_chroma_collection()

    query_result = collection.get(
        where={
            "$and": [
                {"source": source if source is not None else {"$ne": "None"}},

                {"timestamp": {
                    "$gte": datetime.timestamp(start_timestamp) if start_timestamp is not None else 0,
                }
                },

                {"timestamp": {
                    "$lte": datetime.timestamp(end_timestamp),
                }
                },

                # {"level": level if level is not None else {"$ne": "None"}}
            ]
        },

        where_document={
            "$contains": log_string
        }
    )

    return query_result
