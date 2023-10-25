from consts import SIZE
from render.map import Map
from render.stateManagers.StateManager import StateManager


class MapState(StateManager):
    def __init__(self, screen):
        super(MapState, self).__init__(screen)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(Map(0, 0, *SIZE))

    def during_screen(self, dt):
        self.screen.fill((0, 0, 0))
        self.screen.guiRenderer.render(self.screen)