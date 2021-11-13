import pygame.font

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_TYPE, BLACK_COLOR


def get_score_element(points):
    font = pygame.font.Font(FONT_TYPE, 22)
    text = font.render("Points: " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1020, 25)
    return text, text_rect


def get_centered_message(message):
    font = pygame.font.Font(FONT_TYPE, 30)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    return text, text_rect


