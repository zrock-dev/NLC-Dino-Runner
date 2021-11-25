from nlc_dino_runner.components.cloud.cloud_image import Cloud
from pygame.time import get_ticks


class Cloud_manager:
    def __init__(self):
        self.clouds = []

    def update(self):
        if len(self.clouds) <= 4 or self.clouds[-2].rect.x <= 200:
            self.clouds.append(Cloud())

        for cloud in self.clouds:
            cloud.update()
            if not cloud.validity:
                self.clouds.remove(cloud)

    def draw(self, screen):
        object_list = [(cloud.image, cloud.rect) for cloud in self.clouds if
                       cloud.validity]
        screen.blits(object_list)
