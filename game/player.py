import pygame

import loader
from render.gui.base.font import RobotoSlab
from render.gui.base.text import Text


class Player:
    def __init__(self, long, lat, id, name, skin):
        self.long = long
        self.lat = lat
        self.id = id
        self.name = name
        self.skin = skin

    def render(self, screen, x, y):
        textObj = Text(self.name, RobotoSlab.retrieve("bold", 12), (255, 255, 255), (0, 0))
        renderTo = pygame.Surface((50, 50), flags=pygame.SRCALPHA)
        renderTo.blit(loader.load_image(f"skins/hand/{self.skin['left_hand']}"), (25-10-8, 15))
        renderTo.blit(pygame.transform.flip(loader.load_image(f"skins/hand/{self.skin['right_hand']}"), True, False), (25+10-1, 15))
        renderTo.blit(loader.load_image(f"skins/base/{self.skin['base']}"), (9, 9))
        renderTo.blit(loader.load_image(f"skins/hat/{self.skin['hat']}"), (9, 9))
        textObj.centerAt(x, y-25)
        textObj.render(screen)
        screen.blit(renderTo, (x-renderTo.get_width()/2, y-renderTo.get_height()/2))
