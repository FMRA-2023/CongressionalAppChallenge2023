import pygame

import loader
from colors import GRAY, LIGHT_GRAY
from render.gui.base.renderable import Renderable
from render.gui.elements.button import Button


class SkinOption(Button):
    def __init__(self, x, y, part, id, skinState):
        skin = pygame.transform.scale(loader.load_image(f"skins/{part if part not in ['left_hand', 'right_hand'] else 'hand'}/{id}"), (30, 30))
        super().__init__(x, y, [Renderable(pygame.Rect(x, y, 40, 40), GRAY, 10), Renderable(skin, (x+5, y+5))], lambda:None, lambda:None, self.click, self.release)
        self.part = part
        self.id = id
        self.skinState = skinState

    def click(self):
        self.renderables[0].color = LIGHT_GRAY

    def release(self):
        self.renderables[0].color = GRAY
        self.skinState.screen.playerManager.myPlayer.skin[self.part] = self.id