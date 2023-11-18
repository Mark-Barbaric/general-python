from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    l = head
    r = None if not head else head.next

    while l and r:
        cur_next = r.next
        l.next=cur_next
        r.next=l

        if not prev:
            head = r
            
        if prev:
            prev.next = r
        
        prev = l
        l = l.next

        if l:
            r = l.next
        
    
    return head