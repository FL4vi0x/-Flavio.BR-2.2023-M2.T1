import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        # self.Gindex = 0
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(260, 310)
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 9:
            self.step_index = 0
