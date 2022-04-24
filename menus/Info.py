import Presence
import pygame
import json
import Util

def_color = (255, 255, 255)

with open("config.json") as f:
    config = json.load(f)

version = config["version"]


class Info:
    def __init__(self, screen):
        self.name = "info_menu"
        self.screen = screen

    def init_screen(self):
        text = Util.write_text(f"Version ({version})", def_color)
        author = Util.write_text("Game made by Wayvshock", def_color)
        self.screen.blit(text, (500, 300))
        self.screen.blit(author, (450, 330))
        Presence.update_presence("In info menu", "Not playing the game")
        pygame.display.update()
