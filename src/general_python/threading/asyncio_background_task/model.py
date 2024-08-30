from pydantic import BaseModel, ConfigDict


class TestModel(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    name: str
    value: int


class FullModel(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    models: list[TestModel]
