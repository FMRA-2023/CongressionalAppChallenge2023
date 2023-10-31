import geocoder

from colors import GRAY
from consts import NOTCH_SIZE, SIZE
from game.player import Player
from render.gui.base.font import RobotoSlab
from render.gui.elements.textElement import TextElement
from render.gui.loadingSign import LoadingSign
from render.gui.sTextInput import STextInput
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager


class LoginState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)
        self.loggingIn = False
        self.ticket = ""

        self.retrieving = False

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+5, "Samaritans", RobotoSlab.retrieve("bold", 50), (255, 255, 255)), tag="title")
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE+75, "Username", RobotoSlab.retrieve("regular", 18), (255 ,255, 255)), tag="usernameLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE+100), tag="usernameInput")
        guiRenderer.add_element(
            TextElement(10, NOTCH_SIZE + 140, "Password", RobotoSlab.retrieve("regular", 18), (255, 255, 255)),
            tag="passwordLabel")
        guiRenderer.add_element(STextInput(10, NOTCH_SIZE + 165, subchar="*"), tag="passwordInput")
        guiRenderer.add_element(SubmitButton(10, NOTCH_SIZE+210, "Login", self.login), tag="loginButton")
        guiRenderer.add_element(SubmitButton(100, NOTCH_SIZE+210, "...or Sign Up", lambda:self.screen.setState(self.screen.SIGNUP)), tag="loginButton")

    def login(self):
        guiRenderer = self.screen.guiRenderer
        if guiRenderer.has_element("warning"):
            guiRenderer.remove_element("warning")
        self.loggingIn = True
        guiRenderer.add_element(LoadingSign(SIZE[0]/2, NOTCH_SIZE+350, 100), tag="loading")
        self.ticket = self.screen.networking.login(guiRenderer.get_element("usernameInput").text, guiRenderer.get_element("passwordInput").text)
        # self.screen.setState(self.screen.MAP)

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        if self.loggingIn:
            if self.ticket in self.screen.networking.responses.keys():
                if self.screen.networking.responses[self.ticket]["result"]:
                    self.retrieving = True
                    self.ticket = self.screen.networking.retrieve_data(self.screen.guiRenderer.get_element("usernameInput").text)

                else:
                    self.screen.guiRenderer.add_element(TextElement(130, NOTCH_SIZE+75, "Incorrect password or username", RobotoSlab.retrieve("regular", 18), (255, 0, 0)), tag="warning")
                    self.screen.guiRenderer.remove_element("loading")
                self.loggingIn = False


        if self.retrieving:
            if self.ticket in self.screen.networking.responses.keys():
                if self.screen.networking.responses[self.ticket]["result"]:
                    playerData = self.screen.networking.responses[self.ticket]["data"]
                    self.screen.playerManager.players[playerData["player_id"]] = Player.generatePlayer(playerData)
                    self.screen.playerManager.myPlayer = self.screen.playerManager.players[playerData["player_id"]]
                    self.screen.playerManager.myPlayer.lat, self.screen.playerManager.myPlayer.long = geocoder.ip("me").latlng
                    self.screen.playerManager.make_request(self.screen.networking)
                    self.screen.setState(self.screen.MAP)

                self.retrieving = False

        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
