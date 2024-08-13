def test_get_root(test_fast_api_client):
    res = test_fast_api_client.get("/")
    assert res.status_code == 200
    assert res.json() == {'msg': 'Hello World'}
