import random

import pygame.time
from nlc_dino_runner.components.obstacles_main.cactus_child import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS, GAME_SPEED, HEARTS_NUMBER


class ObstacleManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles_list:
            obstacle.update(self.obstacles_list, game)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    pygame.time.delay(100)
                    game.power_up_manager.when_appears = random.randint(200, 500)
                    game.death_count_print = True
                    game.game_speed = GAME_SPEED
                    game.dino_lives.update_list()
                    self.obstacle_reset()
                    if game.dino_lives.trigger:
                        game.points = 0
                        game.death_count += 1
                        game.dino_lives.reset_hearts()
                        game.playing = False
                    break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def obstacle_reset(self):
        self.obstacles_list = []