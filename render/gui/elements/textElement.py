from render.gui.base.element import GuiElement
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text


class TextElement(GuiElement):
    def __init__(self, x, y, text, font, color, centerAt=False):
        textObj = Text(text, font, color, (x, y))
        if centerAt:
            textObj.centerAt(x, y)
        super(TextElement, self).__init__(x, y, [Renderable(textObj)])