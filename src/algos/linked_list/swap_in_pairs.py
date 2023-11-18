from typing import Optional
from src.data_structures.linked_list import LinkedList


def swapPairs(head: Optional[LinkedList]) -> Optional[LinkedList]:
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