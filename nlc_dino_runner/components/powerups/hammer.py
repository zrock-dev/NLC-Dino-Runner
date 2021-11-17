from nlc_dino_runner.components.powerups.power_up import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        self.rect = self.image.get_rect()
        super().__init__(self.image, self.type)
