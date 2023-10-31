from consts import SIZE
from render.map import Map
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab


class MapState(StateManager):
    def __init__(self, screen):
        super(MapState, self).__init__(screen)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(Map(0, 0, *SIZE, self.screen), tag="map")
        create_bottom_tab(self.screen)

    def during_screen(self, dt):
        self.screen.fill((0, 0, 0))
        self.screen.playerManager.update_players(self.screen.networking)
        self.screen.playerManager.update_renders(self.screen.guiRenderer)
        self.screen.guiRenderer.render(self.screen)