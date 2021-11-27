import random
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + self.image.get_width())
        self.rect.y = random.randint(50, 200)
        self.validity = True

    def update(self, clouds_list):
        self.rect.x -= 1
        if self.rect.x < -self.image_width:
            clouds_list.pop(clouds_list.index(self))
