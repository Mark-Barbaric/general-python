from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID, uuid4


class PublishStatus(Enum):
    unpublished = 0
    flagged = 1
    published = 2



class RecipeModel(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str
    description: str
    author: UUID = Field(default_factory=uuid4, frozen=True)
    publish_status : PublishStatus = PublishStatus.unpublished
