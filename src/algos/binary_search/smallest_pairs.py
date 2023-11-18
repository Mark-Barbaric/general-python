import sys
import heapq
from operator import itemgetter

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

    l = 0
    lst = []
    
    ans = []
    
    while k > 0:
        
        top = lst[l]
        value = top[0]
        array = top[1]
        i = l + 1
        
        for i in range(l + 1, len(lst)):
            
            new = lst[i]
            n_value = new[0]
            n_array = new[1]
            
            if array != n_array:
                ans.append([value, n_value])
                k -= 1

            if k == 0:
                break

        l+=1
    return ans