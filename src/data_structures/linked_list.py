from typing import Optional

class LinkedList:
    
    def __init__(self, val:int, next=None):
        self._val = val
        self.next = next


    @property
    def val(self):
        return self._val
    
    