from typing import Optional
from src.data_structures.linked_list import LinkedList


def swapPairs(head: Optional[LinkedList]) -> Optional[LinkedList]:
    prev = None
    left = head
    right = None if not head else head.next

    while left and right:
        cur_next = right.next
        left.next = cur_next
        right.next = left

        if not prev:
            head = right

        if prev:
            prev.next = right

        prev = left
        left = left.next

        if left:
            right = left.next

    return head
