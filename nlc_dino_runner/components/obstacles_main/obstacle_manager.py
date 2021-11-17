import pygame.time
from nlc_dino_runner.components.obstacles_main.cactus_child import Cactus
from nlc_dino_runner.utils.constants import GAME_SPEED

# Image monitor


class ObstacleManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):
        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus())
        for obstacle in self.obstacles_list:
            obstacle.update(self.obstacles_list, game)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles_list.remove(obstacle)
                else:
                    game.power_up_manager.reset_power_ups(game.points)
                    game.death_count_print = True
                    game.dino_lives.update_list()
                    self.reset_obstacle()
                    if game.dino_lives.trigger:
                        pygame.time.delay(100)
                        game.game_speed = GAME_SPEED
                        game.points = 0
                        game.death_count += 1
                        game.dino_lives.reset_hearts_block()
                        game.power_up_manager.reset_power_ups()
                        self.reset_obstacle()
                        game.playing = True
                    break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles_list.clear()
