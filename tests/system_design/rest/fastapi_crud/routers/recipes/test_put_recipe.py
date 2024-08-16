from src.system_design.rest.fastapi_crud.app.model import RecipeModel, PublishStatus


def test_put_recipe_200(test_fast_api_client):
    recipe_id = '00000000-0000-0000-0000-000000000001'
    put_kwargs = {
        'id': recipe_id,
        'name': 'New Recipe Name',
        'description': 'The recipe has been changed',
        'author': '00000000-0000-0000-0000-000000000001',
        'publish_status': PublishStatus.published
    }
    put_recipe_model = RecipeModel(**put_kwargs)
    res = test_fast_api_client.put(f"recipes/{recipe_id}", content=put_recipe_model.model_dump_json())
    assert res.status_code == 200
    updated_recipe = res.json()
    assert updated_recipe['name'] == 'New Recipe Name'
    assert updated_recipe['publish_status'] == 2


def test_put_recipe_422(test_fast_api_client):
    recipe_id = '00000000-0000-0000-0000-000000000001'
    raw_json = {
        'id': recipe_id,
        'description': 'The recipe has been changed',
        'author': '00000000-0000-0000-0000-000000000001',
        'publish_status': 2
    }
    res = test_fast_api_client.put(f"recipes/{recipe_id}", json=raw_json)
    assert res.status_code == 422
