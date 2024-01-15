from bird import Bird
from eating import Eating
from makingsound import MakingSound


class Penguine(Bird, Eating, MakingSound):
    def __init__(self, weight, height, color):
        super().__init__(weight, height, color)

    def eat(self):
        pass

    def makesound(self):
        pass
