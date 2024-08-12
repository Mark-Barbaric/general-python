class User:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def __eq__(self, rhs):
        return self._name == rhs._name and self._age == rhs._age
