from abc import ABC, abstractmethod

class AbstractCollection(ABC):
    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def length(self):
        pass