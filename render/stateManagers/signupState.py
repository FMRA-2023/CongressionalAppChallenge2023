import loader
from colors import GRAY
from consts import NOTCH_SIZE, SIZE
from render.gui.base.font import RobotoSlab
from render.gui.elements.image import Image
from render.gui.elements.textElement import TextElement
from render.gui.loadingSign import LoadingSign
from render.gui.sTextInput import STextInput
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager


class SignupState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)
        self.signingUp = False
        self.ticket = ""

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+5, "iVolunteer", RobotoSlab.retrieve("bold", 50), (255, 255, 255)), tag="title")
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+75, "Username", RobotoSlab.retrieve("regular", 18), (255 ,255, 255)), tag="usernameLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE+100), tag="usernameInput")
        guiRenderer.add_element(
            TextElement(10, NOTCH_SIZE + 140, "Password", RobotoSlab.retrieve("regular", 18), (255, 255, 255)),
            tag="passwordLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE + 165), tag="passwordInput")
        guiRenderer.add_element(SubmitButton(10, NOTCH_SIZE+210, "Sign Up", self.signup), tag="signupButton")
        guiRenderer.add_element(SubmitButton(120, NOTCH_SIZE+210, "...or Log In", lambda:self.screen.setState(self.screen.LOGIN)), tag="loginButton")
        guiRenderer.add_element(Image(SIZE[0]/2-175, SIZE[1]/2-50, loader.load_image("logo", size=(350, 350))))

    def signup(self):
        guiRenderer = self.screen.guiRenderer
        if guiRenderer.has_element("warning"):
            guiRenderer.remove_element("warning")
        self.signingUp = True
        guiRenderer.add_element(LoadingSign(SIZE[0]/2, NOTCH_SIZE+350, 100), tag="loading")
        self.ticket = self.screen.networking.signup(guiRenderer.get_element("usernameInput").text, guiRenderer.get_element("passwordInput").text)
        # self.screen.setState(self.screen.MAP)

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        if self.signingUp:
            if self.ticket in self.screen.networking.responses.keys():
                if self.screen.networking.responses[self.ticket]["result"]:
                    self.screen.setState(self.screen.LOGIN)

                else:
                    self.screen.guiRenderer.add_element(TextElement(150, NOTCH_SIZE+75, "Username taken", RobotoSlab.retrieve("regular", 18), (255, 0, 0)), tag="warning")

                    self.screen.guiRenderer.remove_element("loading")
                self.signingUp = False

        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
