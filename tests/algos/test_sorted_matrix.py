import pytest
from src.algos.binary_search.sorted_matrix import kthSmallest


@pytest.mark.skip(reason="Not implemented yet")
def test_sorted_matrix():
    m1=[[1,2,3,4,5],[6,7,8,9,10],[8,8,8,11,12],[9,10,11,12,12],[12,12,12,12,12]]
    ans = kthSmallest(m1, 2)
    assert(ans) == 2
    m1=[[1,2],[1,3]]
    ans = kthSmallest(m1, 1)
    assert(ans) == 1
