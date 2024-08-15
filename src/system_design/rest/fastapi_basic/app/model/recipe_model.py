from enum import Enum
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class PublishStatus(Enum):
    unpublished = 0
    flagged = 1
    published = 2



class RecipeModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    author: UUID = Field(default_factory=uuid4)
    publish_status : PublishStatus = PublishStatus.unpublished
