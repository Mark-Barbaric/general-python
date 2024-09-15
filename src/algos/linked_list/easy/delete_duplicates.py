from src.data_structures.linked_list import LinkedList
from typing import Optional


def delete_duplicates_from_sorted_list(node: Optional[LinkedList]) -> Optional[LinkedList]:
    if not node:
        return None

    cur = node.next
    prev = node

    while cur:
        while cur and cur.val == prev.val:
            cur = cur.next

        prev.next = cur
        prev = cur
        if cur:
            cur = cur.next

    return node
