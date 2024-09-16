from src.system_design.rest.fastapi_crud.app.model import RecipeModel, PublishStatus
from uuid import uuid4, UUID
from pydantic import ValidationError
import pytest


def test_valid_recipe_model():
    recipe_id = UUID('00000000-0000-0000-0000-222222222222')
    recipe_name = 'Test Recipe'
    recipe_model = RecipeModel(
        id=recipe_id,
        name=recipe_name,
        description="This is a brand new recipe",
        author=uuid4()
    )
    assert recipe_model.name == 'Test Recipe'
    assert str(recipe_model.id) == recipe_id


def test_invalid_recipe_model():

    with pytest.raises(ValidationError) as exc:
        recipe_model = RecipeModel(  # noqa: F841
            id=UUID('00000000-0000-0000-0000-222222222222'),
            name='Test',
            description='New',
        )

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    assert validation_errors[0]['type'] == 'missing'


def test_recipe_model_immutability():
    recipe_model = RecipeModel(
        id=uuid4(),
        name='Test Recipe',
        description="This is a brand new recipe",
        author=uuid4()
    )
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
    recipe_model = RecipeModel(    
        id=uuid4(),
        name='Test Recipe',
        description="This is a brand new recipe",
        author=uuid4(),
        publish_status=PublishStatus.published
    )
    assert recipe_model.publish_status == PublishStatus.published
