from src.system_design.rest.fastapi_crud.app.routers.fake_recipes_db import RECIPES_DB


def test_get_items(test_fast_api_client):
    res = test_fast_api_client.get('/recipes')
    assert res.status_code == 200
    assert res.json() == RECIPES_DB


def test_get_item_200(test_fast_api_client):
    res = test_fast_api_client.get('/recipes/00000000-0000-0000-0000-000000000001')
    assert res.status_code == 200
    res_json = res.json()
    assert len(res_json) == 1
    assert res.json() == RECIPES_DB[0]


def test_get_item_400(test_fast_api_client):
    item_id = '0004'
    res = test_fast_api_client.get(f"/recipes/{item_id}")
    assert res.status_code == 404
    assert res.json() == {'detail': f"Recipe with recipe_id: {item_id} not found"}
