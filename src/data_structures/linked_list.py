class LinkedList:

    def __init__(self, val: int, left_next=None):
        self._val = val
        self.left_next = left_next

    @property
    def val(self):
        return self._val
