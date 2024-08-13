def test_get_items(test_fast_api_client):
    res = test_fast_api_client.get('/items')
    assert res.status_code == 200
    assert res.json() == [{'id': '0001', 'name': 'Item1'}, {'id': '0002', 'name': 'Item2'}]