from pydantic import BaseModel


class AddShemas(BaseModel):
    name: str
    firstname: str
    date: str


class PutSHEMAS(BaseModel):
    name: str
    firstname: str
    date: str
