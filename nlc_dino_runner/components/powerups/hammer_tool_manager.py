import pygame


class HammerToolManager:
    def __init__(self):
        self.dino_status = False  # Does the dino has the hammer power up?
        self.hammer_tools = []

    def update(self, keyboard_input):
        if self.dino_status:
            self.hammer_tools =
            if keyboard_input[pygame.K_SPACE]:  # Is the dino using the hammer?
                pass

    def draw(self):
        pass
