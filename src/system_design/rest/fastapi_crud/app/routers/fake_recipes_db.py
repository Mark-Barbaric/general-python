from typing import Optional
from enum import Enum
from uuid import UUID
from ..model import RecipeModel, PublishStatus


RECIPES_DB: list[RecipeModel] = [
    RecipeModel(
        id=UUID("00000000-0000-0000-0000-000000000001"),
        name='Recipe 1',
        description='This is recipe 1',
        author=UUID("00000000-0000-0000-0000-000000000001"),
        publish_status=PublishStatus.unpublished
    ),
    RecipeModel(
        id=UUID("00000000-0000-0000-0000-000000000002"),
        name='Recipe 2',
        description='This is recipe 2',
        author=UUID("00000000-0000-0000-0000-000000000001"),
        publish_status=PublishStatus.unpublished
    )
]


class RecipeSearchType(int, Enum):
    id = 0
    name = 1


def get_recipe_from_db(search_param: str,
                       recipe_models: list[RecipeModel],
                       search_type=RecipeSearchType.id) -> Optional[RecipeModel]:
    for recipe_model in recipe_models:
        match search_type:
            case RecipeSearchType.id:
                if recipe_model.id == search_param:
                    return recipe_model
            case RecipeSearchType.name:
                if recipe_model.name == search_param:
                    return recipe_model
            case _:
                return None

    return None
