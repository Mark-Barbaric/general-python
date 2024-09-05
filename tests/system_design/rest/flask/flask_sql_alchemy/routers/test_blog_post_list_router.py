def test_200_response(flask_sql_alchemy_test_client):
    res = flask_sql_alchemy_test_client.get('/posts')
    assert res.status_code == 200
    res_json = res.json
    assert len(res.json) == 2
    blog_post_1 = res_json[0]
    assert blog_post_1['blog_post_name'] == 'Post 1'
    assert blog_post_1['author'] == 'mark'
    assert blog_post_1['average_rating'] == 3.75
    blog_post_2 = res_json[1]
    assert blog_post_2['blog_post_name'] == 'Post 2'
    assert blog_post_2['author'] == 'mark'
    assert blog_post_2['average_rating'] == 0.0
