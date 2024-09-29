from typing import Literal


class Stack[T]:
    def __init__(self) -> None:
        self._container: list[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def top(self) -> T:
        return self._container[-1]

    def is_empty(self) -> bool:
        return len(self._container) == 0



class NumericStack[T: (int, float)](Stack[T]):
    def sum(self) -> T | Literal[0]:
        return sum(self._container)
