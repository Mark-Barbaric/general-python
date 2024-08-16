from pydantic import BaseModel, Field, EmailStr, SecretStr, SecretBytes, ConfigDict
from uuid import UUID, uuid4
from enum import Enum


MIN_USER_NAME_LENGTH = 5
MAX_USER_NAME_LENGTH = 12


class UserPermissions(Enum):
    unverified_user = 0
    verified_user = 1
    admin = 1


class UserModel(BaseModel):
    model_config = ConfigDict(extra='forbid')
    user_id: UUID = Field(default_factory=uuid4, frozen=True)
    user_name: str = Field(min_length=MIN_USER_NAME_LENGTH,
                           max_length=MAX_USER_NAME_LENGTH)
    password: SecretStr
    password_bytes: SecretBytes
    email: EmailStr
    user_permissions : UserPermissions = UserPermissions.unverified_user
