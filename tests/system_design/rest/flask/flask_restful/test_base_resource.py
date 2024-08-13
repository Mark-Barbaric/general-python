def test_base_resource(test_flask_client):
    res = test_flask_client.get('/')
    assert res.status_code == 200
    assert res.json == {'message': 'Hellow World'}
