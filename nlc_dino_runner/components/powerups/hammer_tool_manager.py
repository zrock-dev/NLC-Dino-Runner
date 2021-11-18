import pygame
from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class HammerToolManager:
    def __init__(self):
        self.dino_status = False  # Does the dino has the hammer power up?
        self.dino_positions = None
        self.hammer_tool_status = False  # Is any hammer tool in use?
        self.temporal_hammer = None
        self.hammer_tools = [Hammer_Tool()] * 3
        self.hammer_collision = False

    def update(self, keyboard_input, game):
        if self.dino_status:
            if keyboard_input[pygame.K_SPACE] and not self.hammer_tool_status:  # Has the dino thrown the hammer?
                self.hammer_tool_status = True
                self.temporal_hammer = self.hammer_tools.pop()
                self.temporal_hammer.rect.x = self.dino_positions.x
                self.temporal_hammer.rect.y = self.dino_positions.y

            if self.hammer_tool_status:
                self.temporal_hammer.update()
                print('Checking collision')
                if self.temporal_hammer.rect.colliderect(game.obstacle_manager.obstacle_position):
                    game.obstacle_manager.hammer_status = self.hammer_tool_status
                    self.hammer_collision = True
                else:
                    self.hammer_collision = False
                self.hammer_tool_status = False if self.temporal_hammer.rect.x >= SCREEN_WIDTH else True

            if not self.hammer_tools and not self.hammer_tool_status:  # Dino has no more tools :(
                game.power_up_manager.dino_status = False
                self.reset()

    def draw(self, screen):
        if self.hammer_tool_status:
            self.temporal_hammer.draw(screen)

    def reset(self):
        self.dino_status = False
        self.hammer_tools = [Hammer_Tool()] * 3
