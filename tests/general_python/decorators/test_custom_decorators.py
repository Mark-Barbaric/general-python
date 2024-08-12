from src.general_python.decorators.custom_decorators import print_decorator, accepts
import pytest


@print_decorator
def print_hello():
    print("Hello")


@accepts(int, (int, float))
def multiply(a, b):
    return a * b


def test_print_decorator(capsys):
    func = print_hello
    assert func.__name__ == 'print_hello'
    func()
    out, err = capsys.readouterr()  # noqa: E731
    assert out == 'Something was called before the function.\nHello\nSomething was called after the function.\n'  # noqa: E501


def test_accepts():
    func = multiply
    assert func.__name__ == "multiply"
    ans = func(2, 3.5)
    assert ans == 7
    with pytest.raises(AssertionError) as exception:
        _ = multiply("12", 3.2)
    assert str(exception.value) == "arg 12 does not match <class 'int'>"
