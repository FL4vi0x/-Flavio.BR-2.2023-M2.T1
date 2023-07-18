import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        # self.Gindex = 0
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(260, 310)
        # if self.Gindex >= 10:
        #     self.Gindex = 0
        # self.image = BIRD[0] if self.Gindex < 5 else BIRD[1]
        # self.rectz = self.image.get_rect()
        # self.x = 80
        # self.y = 310
        # self.Gindex += 1
