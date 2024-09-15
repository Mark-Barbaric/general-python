from typing import Optional
from enum import IntEnum
from ..model import RecipeModel


RECIPES_DB: list[RecipeModel] = [
    {
        'id': '00000000-0000-0000-0000-000000000001',
        'name': 'Recipe 1',
        'description': 'This is recipe 1',
        'author': '00000000-0000-0000-0000-000000000001',
        'publish_status': 0
    },
    {
        'id': '00000000-0000-0000-0000-000000000002',
        'name': 'Recipe 2',
        'description': 'This is recipe 2',
        'author': '00000000-0000-0000-0000-000000000001',
        'publish_status': 1
    }
]


class RecipeSearchType(IntEnum):
    id = 0
    name = 1


def get_recipe_from_db(search_param: str,
                       model: list[RecipeModel],
                       search_type=RecipeSearchType.id) -> Optional[RecipeModel]:
    key = 'id' if search_type == RecipeSearchType.id else 'name'
    for m in model:
        if m[key] == search_param:
            return m

    return None
