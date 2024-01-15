from bird import Bird
from flying import Flying
from eating import Eating
from makingsound import MakingSound


class Pigeon(Bird, Flying, Eating, MakingSound):
    def __init__(self, weight, height, color):
        super().__init__(weight, height, color)

    def fly(self):
        pass

    def eat(self):
        pass

    def makesound(self):
        pass
