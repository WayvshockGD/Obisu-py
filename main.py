# Constants
from constants.BoardConfig import bConfig
from constants.GameConfig import done, enabled, colors

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

pygame.display.set_caption(f"{name} {version}")

pygame.init()
Presence.init()

startButton = pygame.image.load(Util.get_file_path(path="assets/Begin_Button.jpg"))
startButton = pygame.transform.scale(startButton, (400, 70))

space_img = pygame.image.load(Util.get_file_path("assets/Press_Space.jpg"))
space_img = pygame.transform.scale(space_img, (200, 40))

info_img = pygame.image.load(Util.get_file_path("assets/info.jpg"))
info_img = pygame.transform.scale(info_img, (300, 300))

while not done:
    key = pygame.key.get_pressed()
    pygame.event.pump()

    if key[K_SPACE]:
        print("Pressed space key")
    elif key[K_ESCAPE]:
        done = True

    screen.fill(colors.get("screen"))
    screen.blit(space_img, (500, 470))
    screen.blit(startButton, (400, 400))
    screen.blit(info_img, (100, 300))
    pygame.display.update()
    Presence.update_presence(state_presence="In main menu", desc="Probably playing the game")
