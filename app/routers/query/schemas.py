from pydantic import BaseModel


# Search Response Schema
class SearchResponse(BaseModel):
    ids: list[str]
    documents: list[str]

    class Config:
        from_attributes = True
