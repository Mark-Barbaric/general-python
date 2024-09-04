def test_base_resource(flask_sql_alchemy_test_client):
    res = flask_sql_alchemy_test_client.get('/users')
    assert res.status_code == 200
    assert res.json == []