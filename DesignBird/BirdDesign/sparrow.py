from bird import Bird
from bird import Bird
from crow_sparrow_flyingbehaviour import CrowSparrowFlyingBehaviour
from flying import Flying
from eating import Eating
from makingsound import MakingSound


class Sparrow(Bird, Flying, Eating, MakingSound):
    def __init__(self, weight, height, color):
        super().__init__(weight, height, color)

    def fly(self):
        fb = CrowSparrowFlyingBehaviour()
        fb.make_fly()

    def eat(self):
        pass

    def makesound(self):
        pass
