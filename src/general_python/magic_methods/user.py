class User:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"Name: {self._name}, Age: {self._age}"

    def __eq__(self, rhs):
        return self._name == rhs._name and self._age == rhs._age
