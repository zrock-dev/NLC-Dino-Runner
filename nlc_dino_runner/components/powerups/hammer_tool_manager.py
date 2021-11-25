import pygame
from pygame.time import get_ticks
from nlc_dino_runner.components.powerups.hammer_tool import Hammer_Tool
from nlc_dino_runner.utils.constants import SCREEN_WIDTH, HAMMER
from nlc_dino_runner.utils.text_utils import write_on_screen


class HammerToolManager:
    def __init__(self):
        self.hammer_tools = []
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_collision = False  # Has the hammer collide with any object?
        self.off_screen_counter = 0
        self.keyboard_validator = True
        self.start_time = 0

    def update(self, keyboard_input, game):
        if self.dino_status:  # The dino has the hammer power up

            if keyboard_input[pygame.K_SPACE]:
                if self.keyboard_validator:
                    self.keyboard_validator = False
                    self.set_hammer_tool(game)
                    self.start_time = get_ticks()
                if (get_ticks() - self.start_time) >= 45:
                    self.keyboard_validator = True
                    self.start_time = 0

            for item in self.hammer_tools:
                if item.validity:
                    item.update()
                self.check_collision(game, item)
                if item.rect.x >= SCREEN_WIDTH and item.validity:
                    # self.hammer_collision = False
                    self.off_screen_counter += 1
                    # print(f"-------------------The item {self.hammer_tools.index(item)}, has reach the end")
                    # print(f"-------------------Position: {item.rect.x}")
                    # print(f"-------------------Validity: {item.validity}")

            if self.off_screen_counter >= 3 and not self.hammer_tools[-1].validity:
                # for item in self.hammer_tools:
                #     print(f"Item nro. {self.hammer_tools.index(item)}")
                #     print(f"Final position at reset: {item.rect.x}")
                #     print(f"Validity: {item.validity}")

                # print("Number of items at the end", self.off_screen_counter)
                self.reset()

    def check_collision(self, game, item):
        if item.rect.colliderect(game.obstacle_manager.obstacle_position) and item.validity:
            self.hammer_collision = True
        else:
            self.hammer_collision = False

    def set_hammer_tool(self, game):
        if len(self.hammer_tools) <= 2:
            self.hammer_tools.append(Hammer_Tool(game.player.dino_rect.x, game.player.dino_rect.y))

        if len(self.hammer_tools) == 3:
            game.player.hammer = False
            game.player.hammer_end = True

    def draw(self, screen):
        objects_list = [(HAMMER, item.rect) for item in self.hammer_tools if item.validity]
        hammer_count = write_on_screen(f"{3 - len(self.hammer_tools)}/3", 25, (1015, 35))
        objects_list.append(hammer_count)
        screen.blits(objects_list)

    def reset(self):
        self.off_screen_counter = 0
        self.dino_status = False
        self.hammer_collision = False
        self.hammer_tools.clear()
        print("Hammer manager reseated\n")
