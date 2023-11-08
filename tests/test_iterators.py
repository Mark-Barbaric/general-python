from src.iterators.linked_list import LinkedList
import pytest

def test_iterators(capfd):
    linked_list = LinkedList([1,2,3])
    iterator = iter(linked_list)
    print(next(iterator))
    out, err = capfd.readouterr()
    assert(out == "1\n")
    print(next(iterator))
    out, err = capfd.readouterr()
    assert(out == "2\n")
    print(next(iterator))
    out, err = capfd.readouterr()
    assert(out == "3\n")
    with pytest.raises(StopIteration):
        print(next(iterator))