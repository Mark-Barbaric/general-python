def test_base_resource(flask_sql_alchemy_test_client):
    res = flask_sql_alchemy_test_client.get('/users')
    assert res.status_code == 200
    res_json = res.json
    assert len(res_json) == 3
    assert res_json[0]['user_name'] == 'mark'
    assert res_json[1]['user_name'] == 'john'
    assert res_json[2]['user_name'] == 'peter'
