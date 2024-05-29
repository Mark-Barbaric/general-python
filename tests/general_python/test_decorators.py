from src.general_python.decorators import print_decorator
import pytest


@print_decorator
def print_hello():
    print(f"Hello")


def test_print_decorator(capsys):
    print_hello()
    out, err = capsys.readouterr()
    assert out == 'Something was called before the function.\nHello\nSomething was called after the function.\n'