from abc import ABC, abstractmethod


class Flying(ABC):
    @abstractmethod
    def fly(self):
        pass

