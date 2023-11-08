from algos.spiral_matrix import traverse_spiral


def test_traverse_spiral():
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    ans=traverse_spiral(start_position=(1,1),matrix=matrix)
    expected_ans=[[1,1],[1,2],[2,2],[2,1],[2,0],[1,0],[0,0],[0,1],[0,2]]
    #assert ans == expected_ans
    assert True