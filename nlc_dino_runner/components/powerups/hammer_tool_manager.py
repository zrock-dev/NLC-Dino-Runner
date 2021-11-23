import pygame

from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, HAMMER

class HammerToolManager:
    def __init__(self):
        self.hammer_tools = []
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_collision = False  # Has the hammer collide with any object?
        self.space_counter = 0
        self.counter = 0

    def update(self, keyboard_input, game):
        if self.dino_status:  # The dino has the hammer power up

            if keyboard_input[pygame.K_SPACE]:
                self.space_counter += 1

            if len(self.hammer_tools) <= 3 and self.space_counter == 3:
                self.hammer_tools.append(Hammer_Tool(game.player.dino_rect.x, game.player.dino_rect.y))
                print("The size of the list is", len(self.hammer_tools))
                self.space_counter = 0

                if len(self.hammer_tools) == 3:
                    game.player.hammer = False
                    game.player.hammer_end = True

            for item in self.hammer_tools:
                item.update()
                self.check_collision(game, item)
                if item.rect.x >= SCREEN_WIDTH and item.validity:
                    self.hammer_collision = False
                    self.counter += 1
                    print("-------------------Status in the for loop", self.counter)

            if self.counter >= 3 or len(self.hammer_tools) >= 4:
                for item in self.hammer_tools:
                    print(item.rect.x)
                print("status at the end", self.counter)
                self.reset()

    def check_collision(self, game, item):
        if item.rect.colliderect(game.obstacle_manager.obstacle_position):
            self.hammer_collision = True
        else:
            self.hammer_collision = False

    def draw(self, screen):
        objects_list = [(HAMMER, item.rect) for item in self.hammer_tools if item.rect.x <= SCREEN_WIDTH]
        screen.blits(objects_list)

    def reset(self):
        self.counter = 0
        self.space_counter = 0
        self.dino_status = False
        self.hammer_collision = False
        self.hammer_tools.clear()
        print("Hammer manager reseated\n")
