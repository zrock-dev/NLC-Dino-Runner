import random
from nlc_dino_runner.components.obstacles_main.class_parent import Obstacle
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class Cactus(Obstacle):

    def __init__(self, image_list):  # Init,initializes spaces of memory with data,"self" points to the instanced object
        self.index = random.randint(0, 2)
        self.image_list = image_list
        # self.index = SMALL_CACTUS[self.index]
        super().__init__(self.image_list, self.index)
        self.rect.y = 350
