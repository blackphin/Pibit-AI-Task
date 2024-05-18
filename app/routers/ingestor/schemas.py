from pydantic import BaseModel


class IngestorSchema(BaseModel):
    message: str
    level: int
