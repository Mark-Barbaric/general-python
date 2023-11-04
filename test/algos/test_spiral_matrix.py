from algos.spiral_matrix import traverse_spiral


def test_traverse_spiral():
    matrix1=[[1,2,3],[4,5,6],[7,8,9]]
    expected_matrix=[[1,1],[1,2],[2,2],[2,1],[2,0],[1,0],[0,0],[0,1],[0,2]]
    assert True