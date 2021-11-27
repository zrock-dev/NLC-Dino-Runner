import pygame

from nlc_dino_runner.components.cloud.cloud_manager import Cloud_manager
from nlc_dino_runner.components.dino_lives import Hearts_block
from nlc_dino_runner.components.dinosaurio import Dino
from nlc_dino_runner.components.obstacles_main.obstacle_manager import ObstacleManager
from nlc_dino_runner.components.powerups.hammer_tool_manager import HammerToolManager
from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils import text_utils
from nlc_dino_runner.utils.constants import (
    TITTLE,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    BG,
    FPS,
    GAME_SPEED,
    WHITE_COLOR, CLOUD
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
        self.game_speed = GAME_SPEED
        self.clock = pygame.time.Clock()
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.hammer_tool_manager = HammerToolManager()
        self.dino_lives = Hearts_block()
        self.cloud_manager = Cloud_manager()
        self.points = 0
        self.running = False
        self.death_count = 0
        self.death_count_print = False

    def score(self):
        self.points += 1
        if self.points % 20 == 0:
            self.game_speed += .3

        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.screen.fill(WHITE_COLOR)
        self.print_menu_elements()
        pygame.display.update()
        self.event_handler()

    def print_menu_elements(self):
        text_element, text_element_rect = text_utils.get_centered_message("Press any key to start")
        self.screen.blit(text_element, text_element_rect)
        self.screen.blit(ICON, (475, 150))
        if self.death_count_print:
            text_element, text_element_rect = text_utils.get_centered_message("Death count: " + str(self.death_count))
            self.screen.blit(text_element, (445, 340))

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.cloud_manager.update()
        self.power_up_manager.update(self.points, self.game_speed, self.player, self)
        self.player.update(user_input)
        self.hammer_tool_manager.update(user_input, self)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(WHITE_COLOR)
        self.draw_bg()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        if self.hammer_tool_manager.dino_status:
            self.hammer_tool_manager.draw(self.screen)
        self.dino_lives.draw(self.screen)
        self.cloud_manager.draw(self.screen)
        self.score()
        pygame.display.flip()  # Update all our configs

    def draw_bg(self):
        img_width = BG.get_width()
        self.screen.blit(BG, (self.x_position_bg, self.y_position_bg))  # blit draws a surface on another surface
        self.screen.blit(BG, (img_width + self.x_position_bg, self.y_position_bg))
        if self.x_position_bg <= -img_width:
            self.screen.blit(BG, (img_width + self.x_position_bg, self.y_position_bg))
            self.x_position_bg = 0
        self.x_position_bg -= self.game_speed
