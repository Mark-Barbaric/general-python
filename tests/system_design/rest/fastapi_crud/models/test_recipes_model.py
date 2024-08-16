from src.system_design.rest.fastapi_crud.app.model import RecipeModel, PublishStatus
from uuid import uuid4
from pydantic import ValidationError
import pytest


def test_valid_recipe_model():
    recipe_id = '00000000-0000-0000-0000-222222222222'
    recipe_name = 'Test Recipe'
    kwargs = {
        'id': recipe_id,
        'name': recipe_name,
        'description': "This is a brand new recipe",
        'author': uuid4()
    }
    recipe_model = RecipeModel(**kwargs)
    assert recipe_model.name == 'Test Recipe'
    assert str(recipe_model.id) == recipe_id


def test_invalid_recipe_model():
    kwargs = {
        'id': '00000000-0000-0000-0000-222222222222',
        'name': 'Test',
        'description': 'New',
    }

    with pytest.raises(ValidationError) as exc:
        recipe_model = RecipeModel(**kwargs)  # noqa: F841

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    assert validation_errors[0]['type'] == 'missing'


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


def test_publish_status():
    kwargs = {
        'id': uuid4(),
        'name': 'Test Recipe',
        'description': "This is a brand new recipe",
        'author': uuid4(),
        'publish_status': PublishStatus.published
    }
    recipe_model = RecipeModel(**kwargs)
    assert recipe_model.publish_status == PublishStatus.published
