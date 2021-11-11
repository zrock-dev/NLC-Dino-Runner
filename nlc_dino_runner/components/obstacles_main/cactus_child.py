import random
from nlc_dino_runner.components.obstacles_main.class_parent import Obstacle


class Cactus(Obstacle):

    def __init__(self, png_array):  # Init,initializes spaces of memory with data,"self" points to the instanced object
        self.index = random.randint(0, 2)
        super().__init__(png_array, self.index)
        self.rect.y = 350
