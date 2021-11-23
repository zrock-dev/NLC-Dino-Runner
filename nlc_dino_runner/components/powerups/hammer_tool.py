from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER


class Hammer_Tool(Sprite):
    def __init__(self, x_dino, y_dino):
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = x_dino
        self.rect.y = y_dino + 5

    def update(self):
        self.rect.x += 15
