import random
import pygame

from nlc_dino_runner.components.powerups.hammer import Hammer
from nlc_dino_runner.components.powerups.shield import Shield
from nlc_dino_runner.utils.constants import HAMMER_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 500)
        self.points = 0
        self.dino_status = False  # Does the dino has the hammer power up?

    #     self.option_numbers = list(range(1, 10))

    def reset_power_ups(self, points=0):
        self.power_ups.clear()
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points

        # print(" The actual power up will show at:", self.when_appears)

    def generate_power_ups(self):
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                # print("generating power up at:", self.when_appears)
                self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                # if 1 == 0:
                #     self.power_ups.append(Shield())
                # else:
                self.power_ups.append(Hammer())
                self.dino_status = True
                # print(" The next power up will show at:", self.when_appears)

    def update(self, points, game_speed, player, game):
        self.points = points
        self.generate_power_ups()
        if self.dino_status:
            game.hammer_tool_manager.dino_status = True
            game.hammer_tool_manager.dino_positions = player.dino_rect

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = power_up.type
                power_up.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
