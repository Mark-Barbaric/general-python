class NumbersIterator:
    def __init__(self, lst=[]):
        """_summary_

        Args:
            lst (_type_, optional): _description_. Defaults to empty list.
        """
        self._items = lst
        self._pos = -1

    def __iter__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self

    def __next__(self):
        """_summary_

        Raises:
            StopIteration: _description_

        Returns:
            _type_: _description_
        """
        self._pos += 1
        if self._pos < len(self._items):
            return self._items[self._pos]
        else:
            raise StopIteration


class Stack:
    def __init__(self):
        """_summary_
        """
        self._items = []

    def push(self, val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        self._items.append(val)

    def __getitem__(self, index):
        """_summary_

        Args:
            index (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self._items[index]

    def __len__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return len(self._items)
