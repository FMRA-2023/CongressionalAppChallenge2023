from render.stateManagers.StateManager import StateManager


class LoginState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)

    def on_change(self):
        pass