import pygame
from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class HammerToolManager:
    def __init__(self):
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_tool_status = False  # Is any hammer tool in use?
        self.temporal_hammer = None
        self.hammer_tools = [Hammer_Tool()] * 3
        self.hammer_collision = False

    def update(self, keyboard_input, game):
        if self.dino_status:
            if keyboard_input[pygame.K_SPACE] and not self.hammer_tool_status:  # Has the dino thrown the hammer?
                self.hammer_tool_status = True
                self.temporal_hammer = self.hammer_tools.pop()
                self.temporal_hammer.rect.x = game.player.dino_rect.x
                self.temporal_hammer.rect.y = game.player.dino_rect.y
                if len(self.hammer_tools) == 0:
                    game.player.hammer_off = True

            if self.hammer_tool_status:
                self.temporal_hammer.update()
                if self.temporal_hammer.rect.colliderect(game.obstacle_manager.obstacle_position):
                    game.obstacle_manager.hammer_status = self.hammer_tool_status
                    self.hammer_collision = True
                    print('Collision booom!!!')

                if self.temporal_hammer.rect.x >= SCREEN_WIDTH:
                    self.hammer_tool_status = False
                    game.obstacle_manager.hammer_status = self.hammer_tool_status

            if not self.hammer_tools and not self.hammer_tool_status:  # Dino has no more tools :(
                self.reset()

    def draw(self, screen):
        if self.hammer_tool_status:
            self.temporal_hammer.draw(screen)

    def reset(self):
        self.dino_status = False
        self.hammer_tools = [Hammer_Tool()] * 3
