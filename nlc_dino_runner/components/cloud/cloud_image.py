import random
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH + self.image.get_width(), SCREEN_WIDTH + 500)
        self.rect.y = random.randint(50, 200)
        self.validity = True

    def update(self):
        self.rect.x -= 1.5
        if self.rect.x <= -SCREEN_WIDTH:
            self.validity = False
