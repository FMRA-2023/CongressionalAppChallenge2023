from colors import GRAY
from consts import NOTCH_SIZE, SIZE
from render.gui.base.font import RobotoSlab
from render.stateManagers.StateManager import StateManager
from render.gui.elements.textElement import TextElement
from render.tabGenerator import create_bottom_tab, create_events_tab

class AvailableState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)
    
    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE + 15, "Volunteer Events", RobotoSlab.retrieve("bold", 30), (255, 255, 255)), tag="listTitle")
        create_bottom_tab(self.screen)
        create_events_tab(self.screen)    

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
    