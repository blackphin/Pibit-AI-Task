# System Imports
from datetime import datetime
import pytz

# FastAPI Imports
from fastapi import APIRouter, HTTPException, status

# Pydantic Imports
from typing import Optional

# Schema Imports
from routers.query import schemas

# Services Imports
from routers.query import services

utc = pytz.UTC

router = APIRouter(tags=['Query Interface'], prefix='/query')


# Health Check
@router.get("/healthcheck", status_code=status.HTTP_200_OK)
def current_status():
    return {"status": "Query Interface Active"}


# Query Interface
@router.get("/search", response_model=schemas.SearchResponse, status_code=status.HTTP_200_OK)
def search_logs(
    start_timestamp: Optional[datetime] = None,
    end_timestamp: Optional[datetime] = utc.localize(datetime.now()),
    level: Optional[str] = None,
    log_string: Optional[str] = "level",
    source: Optional[str] = None,
):
    # Check if start timestamp is greater than end timestamp
    if (start_timestamp is not None) and (end_timestamp is not None) and (start_timestamp > end_timestamp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start timestamp cannot be greater than end timestamp"
        )

    elif level == "" or log_string == "" or source == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query parameters cannot be empty"
        )

    # Get the collection
    collection = services.get_chroma_collection()

    # Query the collection
    query_result = collection.get(
        where={
            "$and": [
                # Filter by source
                {"source": source if source is not None else {"$ne": "None"}},

                {"timestamp": {
                    # Filter by start timestamp
                    "$gte": datetime.timestamp(start_timestamp) if start_timestamp is not None else 0,
                }
                },

                {"timestamp": {
                    # Filter by end timestamp
                    "$lte": datetime.timestamp(end_timestamp),
                }
                },
            ]
        },

        where_document={
            "$and": [
                # Filter by log string
                {"$contains": log_string if log_string is not None else "metadata"},

                # Filter by level
                {"$contains": level if level is not None else "metadata"}
            ]
        }
    )

    return {"ids": query_result["ids"], "documents": query_result["documents"]}
