# event name
# company
# description
# address
# experience needed
# minimum age
# maximum age
# featured image
from colors import GRAY, WHITE
from consts import SIZE
from render.gui.base.font import RobotoSlab
from render.gui.elements.textElement import TextElement
from render.gui.lTextInput import LongTextInput
from render.gui.sTextInput import STextInput
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab


class CreateState(StateManager):
    def __init__(self, app):
        super().__init__(app)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()

        guiRenderer.add_element(TextElement(12, 30, "Create New Event", RobotoSlab.retrieve("bold", 30), WHITE))
        guiRenderer.add_element(TextElement(12, 80, "Name", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 100))

        guiRenderer.add_element(TextElement(12, 120, "Company", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 140))

        guiRenderer.add_element(TextElement(12, 160, "Address", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 180))

        guiRenderer.add_element(TextElement(12, 200, "Experience Needed", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 220))

        guiRenderer.add_element(TextElement(12, 240, "Age Range ([min]-[max])", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 260))

        guiRenderer.add_element(TextElement(12, 280, "Link to Image", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 300))

        guiRenderer.add_element(TextElement(12, 320, "Description", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(LongTextInput(12, 340, SIZE[0]-24), tag="desc")

        guiRenderer.add_element(SubmitButton(12, 360, "Create!", lambda:None), tag="createButton")

        create_bottom_tab(self.screen)

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
        guiRenderer.get_element("createButton").moveTo(12, 340+guiRenderer.get_element("desc").h+20)