# Constants
from constants.BoardConfig import bConfig
from constants.GameConfig import done, \
    is_in_main_menu, \
    colors, \
    game_started, \
    is_in_info_menu

from menus.Info import Info
import Util
import Presence
from pygame.locals import *
import pygame
import json

with open("config.json") as f:
    config = json.load(f)

name = config["name"]
version = config["version"]

screen = pygame.display.set_mode((bConfig.get("width"), bConfig.get("height")), 0, 32)


def clear_screen():
    screen.fill(colors.get("screen"))


pygame.display.set_caption(f"{name} {version}")
pygame.display.set_icon(pygame.image.load(Util.get_file_path("assets/Logo.jpg")))

pygame.init()
Presence.init()


# startButton = pygame.image.load(Util.get_file_path("assets/Begin_Button.jpg"))
# startButton = pygame.transform.scale(startButton, (400, 70))

# space_img = pygame.image.load(Util.get_file_path("assets/Press_Space.jpg"))
# space_img = pygame.transform.scale(space_img, (200, 40))

# info_img = pygame.image.load(Util.get_file_path("assets/info.jpg"))
# info_img = pygame.transform.scale(info_img, (300, 300))

def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(Util.get_file_path(file))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()


def make_text(context: str, option: str, where: int):
    screen.blit(Util.write_text(context, (255, 255, 255)), (where, 300))
    screen.blit(Util.write_text(option, (155, 155, 155)), (where, 340))


def update_to_main():
    # screen.blit(space_img, (500, 470))
    # screen.blit(startButton, (400, 400))
    # screen.blit(info_img, (120, 320))
    make_text("Start Game", "Space Key _", 535)
    make_text("Info Screen", "I Key", 300)
    make_text("Exit Game", "ESC Key", 800)
    pygame.display.update()


while not done:
    key = pygame.key.get_pressed()
    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if is_in_main_menu:
        update_to_main()
        Presence.update_presence(state_presence="In main menu", desc="Not playing the game")

        if key[K_SPACE]:
            is_in_main_menu = False
            game_started = True
            clear_screen()
            pygame.display.update()
        elif key[K_ESCAPE]:
            done = True
        elif key[K_i]:
            is_in_info_menu = True
            is_in_main_menu = False
            clear_screen()
            Info(screen=screen).init_screen()

    if is_in_info_menu:
        Presence.update_presence(state_presence="In info menu", desc="Not playing the game")
        if key[K_BACKSPACE]:
            clear_screen()
            is_in_main_menu = True
            is_in_info_menu = False
            update_to_main()

    screen.fill(colors.get("screen"))
