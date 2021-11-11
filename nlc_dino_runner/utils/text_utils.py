import pygame.font

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


def get_score_element(points):
    font = pygame.font.Font("freesansbold.ttf", 22)
    black_color = (0, 0, 0)
    text = font.render("Points: " + str(points), True, black_color)  # Render text?
    text_rect = text.get_rect()
    text_rect.center = (1020, 25)
    return text, text_rect


def get_centered_message(message):
    font = pygame.font.Font("freesansbold.ttf", 30)
    black_color = (0, 0, 0)
    text = font.render(message, True, black_color)  # Render text?
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    return text, text_rect


