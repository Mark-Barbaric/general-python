from typing import Optional
from src.data_structures.linked_list import LinkedList


def swapPairs(head: Optional[LinkedList]) -> Optional[LinkedList]:
    prev = None
    left = head
    right = None if not head else head.left_next

    while left and right:
        cur_next = right.next
        left.left_next = cur_next
        right.next = left

        if not prev:
            head = right

        if prev:
            prev.left_next = right

        prev = left
        left = left.left_next

        if left:
            right = left.left_next

    return head
