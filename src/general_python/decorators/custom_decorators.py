from collections.abc import Callable
import functools


def print_decorator(func: Callable) -> Callable:
    def wrapper() -> Callable:
        print("Something was called before the function.")
        func()
        print("Something was called after the function.")
    return wrapper


def accepts(*types):
    def _check_accepts(f):
        assert len(types) == f.__code__.co_argcount

        @functools.wraps(f)
        def new_f(*args, **kwargs):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), f"arg {a} does not match {t}"
            return f(*args, **kwargs)
        return new_f
    return _check_accepts
