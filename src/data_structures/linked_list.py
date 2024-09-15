class LinkedList:

    def __init__(self, val: int, next_list=None):
        self._val = val
        self.next = next_list

    @property
    def val(self):
        return self._val
