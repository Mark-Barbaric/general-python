def test_200_response(flask_sql_alchemy_test_client, valid_blog_post_id):
    res = flask_sql_alchemy_test_client.get(f'/posts/{valid_blog_post_id}')
    assert res.status_code == 200
    res_json = res.json
    assert res_json['blog_post_name'] == 'Post 1'
    assert res_json['author'] == 'mark'
    assert res_json['average_rating'] == 3.75


def test_404_response(flask_sql_alchemy_test_client):
    res = flask_sql_alchemy_test_client.get('/posts/0001')
    assert res.status_code == 404
    res_json = res.json
    assert res_json == {'message': "blog post with blog_post_id: 0001 not found"}
