import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.LOCAL_ADJUSTMENT_CACTUS = (
            SMALL_CACTUS[0].get_height() - image[0].get_height()
        )

        if SMALL_CACTUS[0].get_height() != image[0].get_height():
            self.rect.y = 325 + self.LOCAL_ADJUSTMENT_CACTUS
        else:
            self.rect.y = 325
