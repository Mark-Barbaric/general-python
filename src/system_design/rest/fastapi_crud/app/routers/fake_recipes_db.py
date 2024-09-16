from typing import Optional
from enum import Enum
from uuid import UUID
from ..model import RecipeModel, PublishStatus


RECIPES_DB: list[RecipeModel] = [
    RecipeModel(
        id=UUID('00000000-0000-0000-0000-000000000001'),
        name='Recipe 1',
        description='This is recipe 1',
        author=UUID('00000000-0000-0000-0000-000000000001'),
        publish_status=PublishStatus.unpublished
    ),
    RecipeModel(
        id=UUID('00000000-0000-0000-0000-000000000002'),
        name='Recipe 2',
        description='This is recipe 2',
        author=UUID('00000000-0000-0000-0000-000000000001'),
        publish_status=PublishStatus.unpublished
    )
]


class RecipeSearchType(Enum):
    id = "id"
    name = "name"


def get_recipe_from_db(search_param: str,
                       models: list[RecipeModel],
                       search_type=RecipeSearchType.id) -> Optional[RecipeModel]:
    key = 'id' if search_type == RecipeSearchType.id else 'name'
    for m in models:
        m_map = m.model_dump()
        if m_map[key] == search_param:
            return m

    return None
