from pydantic import BaseModel
from datetime import datetime, date


class AddShemas(BaseModel):
    name: str
    firstname: str
    date: date


class PutSHEMAS(BaseModel):
    name: str
    firstname: str
    date: date
