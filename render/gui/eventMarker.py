import pygame

import loader
from colors import WHITE
from render.gui.base.font import RobotoSlab
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text
from render.gui.elements.button import Button


class EventMarker(Button):
    def __init__(self, x, y, name, app):
        textObj = Text(name, RobotoSlab.retrieve("regular", 12), (0, 0, 0), (0, 0))
        textObj.centerAt(x, y-12.5)
        self.app = app
        super().__init__(x-textObj.w/2-5, y-10-textObj.h/2-5, [Renderable(pygame.Rect(x-textObj.w/2-5, y-10-textObj.h/2-5, textObj.w+10, textObj.h/2+10), (252, 89, 89), 5),
                                                               Renderable(loader.load_image("down"), (x-5, y-10)),
                                                               Renderable(textObj)
                                                               ],
                         lambda:None, lambda:None, lambda:None, self.click)

    def click(self):
        self.app.setState(self.app.DETAILS)