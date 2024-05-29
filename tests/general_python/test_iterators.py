from src.general_python.iterators import NumbersIterator, Stack
import pytest


@pytest.fixture
def simple_list():
    return ['first', 'second', 'third']


@pytest.fixture
def numbers_iterator(simple_list):
    return NumbersIterator(lst=simple_list)


def test_simple_iterator(simple_list):
    simple_it = iter(simple_list)
    cur = next(simple_it)
    assert cur == 'first'


def test_numbers_iterator_empty_list():
    numbers_iterator = NumbersIterator()
    numbers_it = iter(numbers_iterator)
    with pytest.raises(StopIteration) as exception:
        cur = next(numbers_it)  # noqa: F841
        assert isinstance(exception, StopIteration)


def test_numbers_iterator(numbers_iterator):
    numbers_iter = iter(numbers_iterator)
    cur = next(numbers_iter)
    assert cur == 'first'


def test_stack(simple_list):
    st = Stack()

    for i in simple_list:
        st.push(i)

    assert st[0] == 'first'
    it = iter(st)
    c = next(it)
    assert c == 'first'
