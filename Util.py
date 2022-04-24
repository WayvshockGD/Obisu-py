import os
import pygame

pygame.font.init()

font = pygame.font.SysFont("arial", 30)


def get_file_path(path):
    return f"{os.getcwd()}/{path}"


def write_text(content, color):
    return font.render(content, False, color)
