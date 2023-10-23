from render.gui.base.element import GuiElement
from render.gui.base.renderable import Renderable


class Image(GuiElement):
    def __init__(self, x, y, image):
        super().__init__(x, y, [Renderable(image, (x, y))])