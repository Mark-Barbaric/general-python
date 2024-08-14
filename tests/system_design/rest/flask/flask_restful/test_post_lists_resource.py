def test_get_post_lists_200(test_flask_client):
    res = test_flask_client.get('/posts')
    assert res.status_code == 200
