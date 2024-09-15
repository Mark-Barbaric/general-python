from tests.test_helpers import list_to_linked_list


def test_fixture():
    root = list_to_linked_list([1, 2, 3, 4])
    assert root.val == 1
    assert root.next.val == 2
    assert root.next.next.val == 3
