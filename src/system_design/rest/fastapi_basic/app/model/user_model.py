from pydantic import BaseModel, Field, EmailStr, ConfigDict
from uuid import UUID, uuid4


MIN_USER_NAME_LENGTH = 5
MAX_USER_NAME_LENGTH = 12


class UserModel(BaseModel):
    model_config = ConfigDict(extra='forbid')
    user_id: UUID = Field(default_factory=uuid4, frozen=True)
    user_name: str = Field(min_length=MIN_USER_NAME_LENGTH,
                           max_length=MAX_USER_NAME_LENGTH)
    #password
    email: EmailStr