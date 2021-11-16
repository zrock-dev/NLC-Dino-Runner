import random

import pygame.time
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import SCREEN_WIDTH

# The one who moves the image


class Obstacle(Sprite):

    def __init__(self, png_array, bird_case=False):
        self.bird_case = bird_case
        if bird_case:
            self.counter = 0
            self.bird_list = png_array
            self.bird_image = png_array[0]
        self.image_list = self.bird_image if bird_case else png_array[random.randint(0, 2)]
        self.rect = self.image_list.get_rect()
        self.rect.x = SCREEN_WIDTH + 20
        self.counter = 0
        self.validator = True

    def update(self, img_list, game):
        if self.counter == 30 and self.bird_case:
            self.unpack_bird_list()
            self.validator = False
            self.counter = 0
        self.counter += 1
        self.validator = True

        self.rect.x -= game.game_speed
        if self.rect.x < -self.rect.width:
            img_list.pop()

    def unpack_bird_list(self):
        if self.validator:
            self.bird_image = self.bird_list[0]
        else:
            self.bird_image = self.bird_list[1]

    def draw(self, screen):
        if self.bird_case:
            screen.blit(self.bird_image, self.rect)
        else:
            screen.blit(self.image_list, self.rect)
