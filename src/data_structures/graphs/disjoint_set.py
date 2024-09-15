class DisjointSet:
    def __init__(self, size: int):
        self._size = size
        self._root = [i for i in range(self.size)]

    def __find(self, x):
        return self._root[x]

    def union(self, x: int, y: int):
        root_x = self.__find(x)
        root_y = self.__find(y)

        for i in range(self.size):
            if self._root[i] == root_y:
                self._root[i] = root_x

    def connected(self, x: int, y: int) -> bool:
        return self.__find(x) == self.__find(y)

    @property
    def size(self) -> int:
        return self._size


class DisjointSet2:
    def __init__(self, size: int):
        self._size = size
        self._root = [i for i in range(self.size)]

    def __find(self, x):
        while x != self._root[x]:
            x = self._root[x]
        return x

    def union(self, x: int, y: int):
        root_x = self.__find(x)
        root_y = self.__find(y)

        if root_x != root_y:
            self._root[root_y] = root_x

    def connected(self, x: int, y: int) -> bool:
        return self.__find(x) == self.__find(y)

    @property
    def size(self) -> int:
        return self._size
