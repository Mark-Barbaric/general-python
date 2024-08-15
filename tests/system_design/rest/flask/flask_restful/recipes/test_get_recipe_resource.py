def test_get_recipe_200(test_flask_client):
    res = test_flask_client.get('/recipes/0001')
    assert res.status_code == 200
    assert res.json == {'name': 'Post 1', 'author': 'Mark'}


def test_get_recipe_404(test_flask_client):
    res = test_flask_client.get('/recipes/0005')
    assert res.status_code == 404
