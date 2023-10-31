import pygame
from consts import SIZE
from colors import LIGHT_GREEN, DARK_GREEN, VERY_DARK_GREEN
from render.gui.base.font import RobotoSlab
from render.gui.base.renderable import Renderable
from render.gui.elements.button import Button
from render.gui.base.text import Text

class EventsTab(Button):
    def __init__(self, x, id, app, text):
        self.x = x
        self.textObj = Text(text, RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x, 50))
        super().__init__(x, 0, [Renderable(pygame.Rect(x, 0, SIZE[0] / 3, 50), VERY_DARK_GREEN, 0), Renderable(self.textObj)], lambda:None, lambda:None, lambda:None, self.click)
        self.id = id
        self.app = app
    
    def click(self):
        self.app.setState(self.id)

    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        super().tick(dt, mousePos, mouseClicked, prevClicked, keys, prevKeys)
        if self.app.getState() == self.id:
            self.renderables[0].color = LIGHT_GREEN
        else:
            self.renderables[0].color= VERY_DARK_GREEN
    
    

    