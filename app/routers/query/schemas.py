from pydantic import BaseModel


class SearchResponse(BaseModel):
    ids: list[str]
    documents: list[str]

    class Config:
        from_attributes = True
