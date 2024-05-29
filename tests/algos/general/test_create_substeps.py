from src.algos.general.create_substeps import create_substeps


def test_create_substeps():
    assert not create_substeps([1, 2, 3, 4])
    assert create_substeps([1, 2, 3, 4, 5, 6]) == [[1], [2, 3], [4, 5, 6]]
