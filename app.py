import pygame

from consts import BEZEL, SIZE
from game.player import Player
from render.GuiRenderer import GuiRenderer
from render.stateManagers.loginState import LoginState
from render.stateManagers.mapState import MapState
from render.stateManagers.skinState import SkinState


class Screen(pygame.Surface):
    LOGIN = 0
    MAP = 1
    SKIN = 2
    AVAILABLE = 3
    SIGNED_UP = 4
    CREATED = 5
    QUESTS = 6
    ACCOUNT = 7
    CREATE = 8
    CHAT = 9
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guiRenderer = GuiRenderer(self)
        self.states = {self.LOGIN:LoginState(self),
                       self.MAP:MapState(self),
                       self.SKIN:SkinState(self, Player(0, 0, 0, "frank liu", {"base":0, "hat":1, "left_hand":3, "right_hand":4}))}

        self.last_pressed = pygame.key.get_pressed()
        self.last_clicked = pygame.mouse.get_pressed()

        self.__state = -1
        self.setState(self.SKIN)

    def setState(self, value):
        self.__state = value
        self.states[self.__state].on_change()

    def getState(self):
        return self.__state

    def update(self, dt, keysPressed, mouseClick, mousePos):
        mousePos = list(mousePos)
        mousePos[0]-=BEZEL
        mousePos[1]-=BEZEL

        self.states[self.__state].during_screen(dt)
        self.guiRenderer.tick(dt, mousePos, mouseClick, self.last_clicked, keysPressed, self.last_pressed)
        self.last_pressed = keysPressed
        self.last_clicked = mouseClick
