from abc import ABC, abstractmethod

class Eating(ABC):
    @abstractmethod
    def eat(self):
        pass