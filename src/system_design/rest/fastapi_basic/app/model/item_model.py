from pydantic import BaseModel


class ItemModel(BaseModel):
    id: str
    name: str
