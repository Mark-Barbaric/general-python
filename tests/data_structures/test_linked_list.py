from src.data_structures.linked_list import LinkedList
from tests.test_helpers import list_to_linked_list


def test_linked_list():
    list = [1, 2, 3, 4]
    list_head: LinkedList = list_to_linked_list(list)

    for n in list:
        assert n == list_head.val
        print(f"val {list_head.val}")
        list_head = list_head.next
