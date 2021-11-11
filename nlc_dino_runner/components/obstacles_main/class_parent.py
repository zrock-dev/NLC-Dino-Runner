from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):

    def __init__(self, png_array, index):
        self.unpacked_img = png_array[index]
        self.index = index
        self.rect = self.unpacked_img.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, img_list, game):
        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            img_list.pop()

    def draw(self, screen):
        screen.blit(self.unpacked_img, self.rect)
