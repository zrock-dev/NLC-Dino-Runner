import pygame
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    BG,
    FPS
)


class Game:
    def __init__(self):
        pygame.init()
        self.playing = False
        pygame.display.set_caption(TITTLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Tuple of width and height
        self.x_position_bg = 0
        self.y_position_bg = 400
        self.game_speed = 20
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_bg()
        pygame.display.flip()  # Update all our configs

    def draw_bg(self):
        img_width = BG.get_width()
        self.screen.blit(BG, (self.x_position_bg, self.y_position_bg))  # blit draws a surface on another surface
        self.screen.blit(BG, (img_width + self.x_position_bg, self.y_position_bg))
        if self.x_position_bg <= -img_width:
            self.screen.blit(BG, (img_width + self.x_position_bg, self.y_position_bg))
            self.x_position_bg = 0
        self.x_position_bg -= self.game_speed