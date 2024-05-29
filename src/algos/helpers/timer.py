from collections.abc import Callable
import functools
import time


def timer(func: Callable):
    @functools.wraps(func)
    def print_time(*args, **kwargs):
        start_time = time.perf_counter()
        ans = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Finished {func.__name__}() in {total_time:.4f} secs")
        return ans
    return print_time