import pygame
import random
from dino_runner.components import obstacles
from dino_runner.components.dinosaur import Y_POS
from dino_runner.components.obstacles.bird import Bird

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

# from dino_runner.utils.constants import LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.index = 0
        self.Y = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            if self.index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.index == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))

        self.index = random.randint(0, 2)
        if self.index > 2:
            self.index = 0
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1200)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
