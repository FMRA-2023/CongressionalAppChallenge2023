import pygame

import loader
from colors import LIGHT_GREEN, DARK_GREEN, VERY_DARK_GREEN
from consts import SIZE
from render.gui.base.renderable import Renderable
from render.gui.elements.button import Button


class ScreenTab(Button):
    def __init__(self, x, id, app):
        super().__init__(x, SIZE[1]-50, [Renderable(pygame.Rect(x, SIZE[1]-50, SIZE[0]/4, 50), VERY_DARK_GREEN, 0), Renderable(loader.load_image(f"icons/{id}", size=(35, 35)), (x+SIZE[0]/8-35/2, SIZE[1]-50+25-35/2))], lambda:None, lambda:None, lambda:None, self.click)
        self.id = id
        self.app = app
    def click(self):
        self.app.setState(self.id)
    
    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        super().tick(dt, mousePos, mouseClicked, prevClicked, keys, prevKeys)
        if self.app.getState() == self.id:
            self.renderables[0].color = LIGHT_GREEN

        else:
            self.renderables[0].color = VERY_DARK_GREEN


