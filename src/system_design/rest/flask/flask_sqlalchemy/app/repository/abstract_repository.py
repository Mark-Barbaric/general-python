from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abstractmethod
    def get_list(self):
        raise NotImplementedError
