from abc import ABC, abstractmethod


class FlyingBehaviour(ABC):
    @abstractmethod
    def make_fly(self):
        pass
