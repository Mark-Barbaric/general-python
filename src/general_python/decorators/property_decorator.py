class PropertyObject(object):
    def __init__(self, count=0):
        self._count = count

    @property
    def count(self):
        return self._count