def test_200_response(flask_sql_alchemy_test_client, valid_user_id):
    res = flask_sql_alchemy_test_client.get(f'/users/{valid_user_id}')
    assert res.status_code == 200
    res_json = res.json
    assert res_json['user_name'] == 'mark'


def test_404_response(flask_sql_alchemy_test_client):
    res = flask_sql_alchemy_test_client.get('/users/0001')
    assert res.status_code == 404
    res_json = res.json
    assert res_json == {'message': "user with user_id: 0001 not found"}
