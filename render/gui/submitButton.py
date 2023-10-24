import pygame

from colors import DARK_GREEN, LIGHT_GREEN
from render.gui.base.font import RobotoSlab
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text
from render.gui.elements.button import Button


class SubmitButton(Button):
    def __init__(self, x, y, text, click_func):
        textObj = Text(text, RobotoSlab.retrieve("regular", 20), (255, 255, 255), (0, 0))
        textObj.centerAt(x+(textObj.w+30)/2, y+(textObj.h+10)/2)
        super().__init__(x, y, [Renderable(pygame.Rect(x, y, textObj.w+30, textObj.h+10), DARK_GREEN, 10),
                                Renderable(textObj)], lambda:None, lambda:None, self.__release, self.__unrelease)
        self.click_func = click_func

    def __release(self):
        self.renderables[0].color = LIGHT_GREEN

    def __unrelease(self):
        self.renderables[0].color = DARK_GREEN
        self.release_func()