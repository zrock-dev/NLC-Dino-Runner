from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART, HEARTS_NUMBER


# HEART width = 27
# HEART height = 25


class Hearts_block(Sprite):
    def __init__(self):
        self.image = HEART
        self.image_width = HEART.get_width()
        self.hearts_number = HEARTS_NUMBER
        self.trigger = False
        # Making up lists
        coord_list = [(x * self.image_width, 30) for x in range(1, self.hearts_number + 1)]
        self.image_list = [(HEART, coord) for coord in coord_list]
        print(self.image_list)

    def draw(self, screen):
        self.trigger = False if not self.hearts_number <= 1 else True
        screen.blits(self.image_list)

    def update_list(self):
        self.image_list.pop()
        self.hearts_number -= 1
        print(self.image_list)

    def reset_hearts(self):
        self.hearts_number = HEARTS_NUMBER
        coord_list = [(x * self.image_width, 30) for x in range(1, self.hearts_number + 1)]
        self.image_list = [(HEART, coord) for coord in coord_list]
