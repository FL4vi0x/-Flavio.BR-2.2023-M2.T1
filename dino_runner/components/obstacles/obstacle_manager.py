from email.policy import default
import pygame
import random

from dino_runner.utils.constants import RUNNING
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
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(1000)
                    game.playing = False
                    game.death_count += 1

                    break
                elif game.player.type == "shield":
                    pass
                elif game.player.type == "hammer":
                    self.obstacles.remove(obstacle)
                elif game.player.type == "partyhat":
                    pygame.time.delay(550)
                    self.obstacles.remove(obstacle)
                    game.player.has_power_up = False
                    game.player.type = "default"

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
