from uuid import uuid4


def test_200_response(test_fast_api_client):
    new_recipe_json = {
        'id': str(uuid4()),
        'name': 'Exciting new recipe',
        'description': 'This is completely new',
        'author': str(uuid4())
    }
    res = test_fast_api_client.post('/recipes', json=new_recipe_json)
    assert res.status_code == 201


def test_409_response(test_fast_api_client):
    recipe_id = '00000000-0000-0000-0000-000000000001'
    new_recipe_json = {
        'id': recipe_id,
        'name': 'Exciting new recipe',
        'description': 'This is completely new',
        'author': str(uuid4())
    }
    res = test_fast_api_client.post('/recipes', json=new_recipe_json)
    assert res.status_code == 409
    assert res.json()['detail'] == f"Recipe with recipe_id: {recipe_id} already exists"

    recipe_name = 'Recipe 1'
    new_recipe_json = {
        'id': '00000000-0000-0000-0000-000000000013',
        'name': recipe_name,
        'description': 'This is completely new',
        'author': str(uuid4())
    }
    res = test_fast_api_client.post('/recipes', json=new_recipe_json)
    assert res.status_code == 409
    assert res.json()['detail'] == f"Recipe with name: {recipe_name} already exists"
