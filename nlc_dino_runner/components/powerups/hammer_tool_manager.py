import pygame

from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, HAMMER

class HammerToolManager:
    def __init__(self):
        self.hammer_tools = []
        self.items_counter = 0
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_collision = False  # Has the hammer collide with any object?
        self.space_counter = 0

    def update(self, keyboard_input, game):
        if self.dino_status:  # The dino has the hammer power up
            if keyboard_input[pygame.K_SPACE]:
                self.space_counter += 1

            if len(self.hammer_tools) <= 3 and self.space_counter == 3:
                self.hammer_tools.append(Hammer_Tool(game.player.dino_rect.x, game.player.dino_rect.y))
                self.items_counter += 1
                print("hammer thrown: Left", 3 - self.items_counter)
                self.space_counter = 0

            for item in self.hammer_tools:
                item.update()
                self.check_collision(game, item)
                if item.rect.x >= SCREEN_WIDTH:
                    self.hammer_tools.remove(item)
                    self.hammer_collision = False

            if self.items_counter == 3 and not self.hammer_tools:
                game.player.hammer = False
                game.player.hammer_end = True
                self.reset()

            print("Times space is pressed:", self.space_counter)

    def check_collision(self, game, item):
        if item.rect.colliderect(game.obstacle_manager.obstacle_position):
            self.hammer_collision = True
        else:
            self.hammer_collision = False

    def draw(self, screen):
        objects_list = [(HAMMER, item.rect) for item in self.hammer_tools]
        screen.blits(objects_list)

    def reset(self):
        self.dino_status = False
        self.hammer_collision = False
        self.hammer_tools = []
