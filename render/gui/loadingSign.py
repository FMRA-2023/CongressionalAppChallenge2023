import math

import pygame

from colors import LIGHT_GREEN
from render.gui.base.element import GuiElement


class LoadingSign(GuiElement):
    def __init__(self, x, y, radius):
        super(LoadingSign, self).__init__(x, y, [])
        self.angle = 0
        self.radius = radius

    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        self.angle += 360 * dt
        self.angle %= 360

    def render(self, screen):
        radius = self.radius
        pygame.draw.arc(screen, LIGHT_GREEN, pygame.Rect(self.x-radius, self.y-radius, 2*radius, 2*radius), math.radians(self.angle), math.radians(self.angle + 10 + (math.sin(math.radians(self.angle))+1)/2*90), width=round(self.radius/5))
