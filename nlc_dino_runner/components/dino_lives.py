from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART, HEARTS_NUMBER
from pygame.time import get_ticks

# HEART width = 27
# HEART height = 25
from nlc_dino_runner.utils.text_utils import write_on_screen


class Hearts_block(Sprite):
    def __init__(self):
        self.image = HEART
        self.image_width = HEART.get_width()
        self.hearts_number = HEARTS_NUMBER
        self.trigger = False
        self.image_y_pos = 20
        # Making up lists
        coord_list = [(x * self.image_width, self.image_y_pos) for x in range(1, self.hearts_number + 1)]
        self.images_list = [(HEART, coord) for coord in coord_list]
        self.temporary_list = self.images_list.copy()
        # -----Message stuff
        self.message = write_on_screen(f"Life lost", 20, (59, 50))
        self.show_message = False
        # -----Message stuff

        # --------Time Stuff
        self.start_time = 0
        # --------Time Stuff

    def draw(self, screen):
        if self.show_message:
            self.set_message_screen()
        screen.blits(self.temporary_list)

    def update_list(self):
        self.trigger = False if not self.hearts_number <= 1 else True
        self.hearts_number -= 1
        # -----Message stuff
        if not self.show_message:
            self.temporary_list.append(self.message)
        self.show_message = True
        self.message[1].x -= 9
        # -----Message stuff
        # --------------------Time Stuff
        self.start_time = get_ticks()
        self.temporary_list.remove(self.temporary_list[-2])
        # --------Time Stuff

    def set_message_screen(self):
        if (get_ticks() - self.start_time) >= 280 and self.show_message:
            self.temporary_list.remove(self.message)
            self.start_time = 0
            self.show_message = False

    def reset_hearts_block(self):
        self.hearts_number = HEARTS_NUMBER
        self.temporary_list = self.images_list.copy()
        self.start_time = 0
        self.show_message = False
        self.message[1].x = 59
