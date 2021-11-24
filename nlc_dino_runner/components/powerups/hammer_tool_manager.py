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

            if len(self.hammer_tools) <= 2 and self.space_counter == 3:
                self.hammer_tools.append(Hammer_Tool(game.player.dino_rect.x, game.player.dino_rect.y))
                print("The size of the list is", len(self.hammer_tools))
                self.space_counter = 0

                if len(self.hammer_tools) == 3:
                    game.player.hammer = False
                    game.player.hammer_end = True

            for item in self.hammer_tools:
                if item.validity:
                    item.update()
                self.check_collision(game, item)
                if item.rect.x >= SCREEN_WIDTH and item.validity:
                    self.hammer_collision = False
                    self.counter += 1
                    print(f"-------------------The item {self.hammer_tools.index(item)}, has reach the end")
                    print(f"-------------------Position: {item.rect.x}")
                    print(f"-------------------Validity: {item.validity}")

            if self.counter >= 3 and not self.hammer_tools[-1].validity:
                for item in self.hammer_tools:
                    print(f"Item nro. {self.hammer_tools.index(item)}")
                    print(f"Final position at reset: {item.rect.x}")
                    print(f"Validity: {item.validity}")

                print("Number of items at the end", self.counter)
                self.reset()

    def check_collision(self, game, item):
        if item.rect.colliderect(game.obstacle_manager.obstacle_position):
            self.hammer_collision = True
        else:
            self.hammer_collision = False

    def draw(self, screen):
        objects_list = [(HAMMER, item.rect) for item in self.hammer_tools if item.validity]
        screen.blits(objects_list)

    def reset(self):
        self.counter = 0
        self.space_counter = 0
        self.dino_status = False
        self.hammer_collision = False
        self.hammer_tools.clear()
        print("Hammer manager reseated\n")
