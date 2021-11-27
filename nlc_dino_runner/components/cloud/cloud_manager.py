from nlc_dino_runner.components.cloud.cloud_image import Cloud
from pygame.time import get_ticks


class Cloud_manager:
    def __init__(self):
        self.clouds = []
        self.cloud_add = True
        self.start_time = 0

    def update(self):
        if self.cloud_add and len(self.clouds) < 4:
            self.cloud_add = False
            self.clouds.append(Cloud())
            print('Cloud added')
            self.start_time = get_ticks()
        if (get_ticks() - self.start_time) >= 5000:
            self.cloud_add = True
            self.start_time = 0

        for cloud in self.clouds:
            cloud.update(self.clouds)

    def draw(self, screen):
        object_list = [(cloud.image, cloud.rect) for cloud in self.clouds if
                       cloud.validity]
        screen.blits(object_list)
