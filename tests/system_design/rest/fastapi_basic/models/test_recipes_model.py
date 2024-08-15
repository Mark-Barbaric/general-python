from src.system_design.rest.fastapi_basic.app.model import RecipeModel
from uuid import uuid4


def test_valid_recipe_model():
    kwargs = {
        'id': uuid4(),
        'name': 'Test Recipe',
        'description': "This is a brand new recipe",
        'author': uuid4()
    }
    recipe_model = RecipeModel(**kwargs)
    assert recipe_model.name == 'Test Recipe'
