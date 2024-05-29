class DisjointSet:
    def __init__(self, size: int):
        self._size = size
        self._root = [i for i in range(self.size)]

    def __find(self, x):
        return self._root[x]

    def union(self, x: int, y: int):
        rootX = self.__find(x)
        rootY = self.__find(y)

        for i in range(self.size):
            if self._root[i] == rootY:
                self._root[i] = rootX

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
        rootX = self.__find(x)
        rootY = self.__find(y)

        if rootX != rootY:
            self._root[rootY] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.__find(x) == self.__find(y)

    @property
    def size(self) -> int:
        return self._size
