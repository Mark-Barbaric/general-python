from collections.abc import Callable


def print_decorator(func: Callable) -> Callable:
    def wrapper() -> Callable:
        print(f"Something was called before the function.")
        func()
        print(f"Something was called after the function.")
    return wrapper