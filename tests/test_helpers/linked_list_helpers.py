from src.data_structures.linked_list import LinkedList


def list_to_linked_list(nums: list[int]) -> LinkedList:
    root = LinkedList(nums[0])
    head = root

    for i in range(1, len(nums)):
        new_node = LinkedList(nums[i])
        head.next = new_node
        head = head.next
    return root


def linked_list_to_list(root: LinkedList) -> list[int]:
    ans = []
    cur = root

    while cur:
        ans.append(cur.val)
        cur = cur.next

    return ans
