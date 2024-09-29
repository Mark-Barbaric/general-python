from tests.test_helpers import list_to_linked_list


def test_linked_list():
    linked_list_as_list: list[int] = [1, 2, 3, 4]
    list_head = list_to_linked_list(linked_list_as_list)

    for n in linked_list_as_list:
        assert list_head
        assert n == list_head.val
        print(f"val {list_head.val}")
        list_head = list_head.next
