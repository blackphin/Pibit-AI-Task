from email import message
from pydantic import BaseModel


class IngestorSchema(BaseModel):
    message: str
    level: int
