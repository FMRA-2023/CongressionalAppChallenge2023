import pygame

from consts import SIZE
from render.gui.base.renderable import Renderable
from render.gui.elements.button import Button


class PlayerIcon(Button):
    def __init__(self, id):
        super().__init__(-100, -100, [Renderable(pygame.Surface((70, 70)), (-100, -100))], lambda:None, lambda:None, lambda:None, lambda:None)
        self.id = id

    def update(self, x, y, img):
        self.moveTo(x, y)
        self.renderables[0].disp = img