from src.algos.graphs.paths.easy_algos import find_the_town_judge_optimized


def test_no_judge():
    trust = [[1, 2], [2, 1]]
    assert find_the_town_judge_optimized(2, trust) == -1
    trust = []
    assert find_the_town_judge_optimized(2, trust) == -1
    trust = [[1, 2], [3, 2], [4, 2], [2, 1]]
    assert find_the_town_judge_optimized(4, trust) == -1


def test_one_person():
    trust = []
    assert find_the_town_judge_optimized(1, trust) == 1


def test_contains_judge():
    trust = [[1, 2]]
    assert find_the_town_judge_optimized(2, trust) == 2
    trust = [[1, 2], [3, 2], [1, 3]]
    assert find_the_town_judge_optimized(3, trust) == 2
    trust = [[1, 3], [2, 3]]
    assert find_the_town_judge_optimized(3, trust) == 3


def test_contains_judge_hard():
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    assert find_the_town_judge_optimized(4, trust) == 3
