from src.algos.binary_search.smallest_pairs import kSmallestPairs

def test_smallest_pairs():
    nums1=[1,7,11]
    nums2=[2,4,6]
    ans=kSmallestPairs(nums1=nums1, nums2=nums2, k=3)
    assert sorted(ans) == sorted([[1,2],[1,4],[1,6]])
    
    nums1=[1,7,11]
    nums2=[2,4,6]
    ans=kSmallestPairs(nums1=nums1, nums2=nums2, k=5)
    assert sorted(ans) == sorted([[1,2],[1,4],[1,6],[2,7],[2,11]])
    
    
    nums1=[1,1,2]
    nums2=[1,2,3]
    ans=kSmallestPairs(nums1=nums1, nums2=nums2, k=2)
    assert sorted(ans) == sorted([[1,1],[1,1]])