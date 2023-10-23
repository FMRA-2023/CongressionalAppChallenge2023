from render.gui.base.font import RobotoSlab
from render.gui.base.text import Text
from render.gui.elements.textinput import TextInput


class STextInput(TextInput):
    def __init__(self, x, y, subchar=""):
        super().__init__(x, y, Text("", RobotoSlab.retrieve("light", 12), (0, 0, 0), (x,y)), maxLen=10, subchar=subchar)