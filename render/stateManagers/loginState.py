from consts import NOTCH_SIZE, SIZE
from render.gui.base.font import RobotoSlab
from render.gui.elements.textElement import TextElement
from render.gui.loadingSign import LoadingSign
from render.gui.sTextInput import STextInput
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager


class LoginState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+5, "Samaritans", RobotoSlab.retrieve("bold", 50), (255, 255, 255)), tag="title")
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+75, "Username", RobotoSlab.retrieve("regular", 18), (255 ,255, 255)), tag="usernameLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE+100), tag="usernameInput")
        guiRenderer.add_element(
            TextElement(10, NOTCH_SIZE + 140, "Password", RobotoSlab.retrieve("regular", 18), (255, 255, 255)),
            tag="passwordLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE + 165), tag="passwordInput")
        guiRenderer.add_element(SubmitButton(10, NOTCH_SIZE+210, "Login", self.login), tag="loginButton")

    def login(self):
        self.screen.guiRenderer.add_element(LoadingSign(120, NOTCH_SIZE+227, 20), tag="loading")
        self.screen.setState(self.screen.MAP)

    def during_screen(self, dt):
        self.screen.fill((25, 25, 25))
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
