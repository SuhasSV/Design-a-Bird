from abc import ABC, abstractmethod


class MakingSound(ABC):
    @abstractmethod
    def makesound(self):
        pass
