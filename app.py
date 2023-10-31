import pygame

from consts import BEZEL, SIZE
from game.PlayerManager import PlayerManager
from game.VolunteerManager import VolunteerManager
from game.player import Player
from networking.networking import Networking
from render.GuiRenderer import GuiRenderer
from render.stateManagers.createState import CreateState
from render.stateManagers.loginState import LoginState
from render.stateManagers.mapState import MapState
from render.stateManagers.profileState import ProfileState
from render.stateManagers.signupState import SignupState
from render.stateManagers.skinState import SkinState
from render.stateManagers.availableState import AvailableState
from render.stateManagers.createdEventsState import CreatedEventsState
from render.stateManagers.registeredEventsState import RegisteredEventsState


class Screen(pygame.Surface):
    LOGIN = 0
    MAP = 1
    SKIN = 2
    AVAILABLE = 3
    DETAILS = 4
    SIGNUP = 6
    ACCOUNT = 7
    CREATE = 8
    CREATED_EVENTS = 9
    SIGNED_UP_EVENTS = 10
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guiRenderer = GuiRenderer(self)
        self.playerManager = PlayerManager()
        self.volunteerManager = VolunteerManager()
        self.networking = Networking()
        self.states = {self.LOGIN:LoginState(self),
                       self.MAP:MapState(self),
                       self.SKIN:SkinState(self),
                       self.CREATE:CreateState(self),
                       self.ACCOUNT:ProfileState(self),
                       self.AVAILABLE:AvailableState(self),
                       self.CREATED_EVENTS:CreatedEventsState(self),
                       self.SIGNED_UP_EVENTS:RegisteredEventsState(self),
                       self.SIGNUP:SignupState(self)}

        self.last_pressed = pygame.key.get_pressed()
        self.last_clicked = pygame.mouse.get_pressed()

        self.__state = -1
        self.setState(self.LOGIN)

    def setState(self, value):
        self.__state = value
        self.states[self.__state].on_change()

    def getState(self):
        return self.__state

    def update(self, dt, keysPressed, mouseClick, mousePos):
        mousePos = list(mousePos)
        mousePos[0]-=BEZEL
        mousePos[1]-=BEZEL

        self.guiRenderer.tick(dt, mousePos, mouseClick, self.last_clicked, keysPressed, self.last_pressed)
        self.states[self.__state].during_screen(dt)
        self.last_pressed = keysPressed
        self.last_clicked = mouseClick
