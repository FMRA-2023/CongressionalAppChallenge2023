# event name
# company
# description
# address
# experience needed
# minimum age
# maximum age
# featured image
from colors import GRAY
from render.stateManagers.StateManager import StateManager


class CreateState(StateManager):
    def __init__(self, app):
        super().__init__(app)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)