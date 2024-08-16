from ..model import RecipeModel
from.fake_users_db import USER_DB
from typing import Optional



RECIPES_DB : list[RecipeModel] = [
    {
        'id': '0001-0001-00000000-0001-0001',
        'name': 'Recipe 1',
        'description': 'This is recipe 1',
        'author': USER_DB[0]['user_id']
    },
    {
        'id': '0001-0001-00000000-0001-0002',
        'name': 'Recipe 2',
        'description': 'This is recipe 2',
        'author': USER_DB[0]['user_id']
    }
]


def get_recipe_with_id(recipe_id: str, model: list[RecipeModel]) -> Optional[RecipeModel]:
    for m in model:
        if m['id'] == recipe_id:
            return m

    return None
