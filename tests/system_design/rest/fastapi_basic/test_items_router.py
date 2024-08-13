def test_get_items(test_fast_api_client):
    res = test_fast_api_client.get('/items')
    assert res.status_code == 200
    assert res.json() == [{'id': '0001', 'name': 'Item1'}, {'id': '0002', 'name': 'Item2'}]


def test_get_item_200(test_fast_api_client):
    res = test_fast_api_client.get('/items/0001')
    assert res.status_code == 200
    assert res.json() == {'id': '0001', 'name': 'Item1'}


def test_get_item_400(test_fast_api_client):
    item_id = '0004'
    res = test_fast_api_client.get(f"/items/{item_id}")
    assert res.status_code == 404
    assert res.json() == {'detail': f"Item with item_id: {item_id} not found"}
