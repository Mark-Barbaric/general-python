def return_squares(l1: list[int]) -> list[int]:
    """_summary_

    Args:
        l (list[int]): _description_

    Returns:
        list[int]: _description_
    """
    # three scenarios
    # empty
    # only negative
    # only positive
    # positive and negative - special case
    
    ## empty
    
    if len(l1) == 0:
        return []
    
    ## only positive
    if l1[0] >= 0:
        return [i ** 2 for i in l1]

    i = 0
    ans = [-1 for _ in range(len(l1))]
    
    l = 0
    
    while l < len(l1) and l1[l] < 0:
        l += 1
    
    # iterate back
    l -= 1
    r = l + 1
    
    while i < len(ans):
        negative_num = None if l < 0 else l1[l]
        positive_num = None if r >= len(l1) else l1[r]
        
        if not negative_num:
            ans[i] = positive_num ** 2
            r += 1
        elif not positive_num:
            ans[i] = negative_num ** 2
            l -= 1
        elif positive_num and negative_num:
            if abs(positive_num) >= abs(negative_num):
                ans[i] = positive_num ** 2
                r += 1
            else:
                ans[i] = negative_num ** 2
                l -= 1
        
        #ans[i] = 
        # l-=1
        
        #ans[i]
        # r += 1
        i += 1

    return ans