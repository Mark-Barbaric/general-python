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
        if(self._pos < len(self._items)):
            return self._items[self._pos]
        else:
            raise StopIteration