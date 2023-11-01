from render.stateManagers.StateManager import StateManager
from colors import GRAY

class EventInformationState(StateManager):

    def __init__(self, screen):
        super().__init__(screen)
    
    def on_change(self):
        return super().on_change()

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
