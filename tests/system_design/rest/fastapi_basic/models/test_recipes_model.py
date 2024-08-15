from src.system_design.rest.fastapi_basic.app.model import RecipeModel
from uuid import uuid4
from pydantic import ValidationError
import pytest


def test_valid_recipe_model():
    kwargs = {
        'id': uuid4(),
        'name': 'Test Recipe',
        'description': "This is a brand new recipe",
        'author': uuid4()
    }
    recipe_model = RecipeModel(**kwargs)
    assert recipe_model.name == 'Test Recipe'


def test_recipe_model_immutability():
    kwargs = {
        'id': uuid4(),
        'name': 'Test Recipe',
        'description': "This is a brand new recipe",
        'author': uuid4()
    }
    recipe_model = RecipeModel(**kwargs)
    with pytest.raises(ValidationError) as exc:
        recipe_model.id = uuid4()

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    assert validation_errors[0]['type'] == 'frozen_field'
    
    with pytest.raises(ValidationError) as exc:
        recipe_model.author = uuid4()

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    assert validation_errors[0]['type'] == 'frozen_field'
