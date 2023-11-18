from src.algos.linked_list.swap_in_pairs import ListNode, swapPairs

def list_to_linked_list(nums : list[int]) -> ListNode:
    root = ListNode(nums[0])
    head = root
    
    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        head.next=new_node
        head = head.next
    
    
    return root
    

def test_fixture():
    root = list_to_linked_list([1,2,3,4])
    assert root.val == 1
    assert root.next.val == 2
    assert root.next.next.val == 3


def test_swap_in_pairs():
    root = list_to_linked_list([1,2])
    swapped_root = swapPairs(root)