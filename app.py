import pygame

from render.GuiRenderer import GuiRenderer
from render.stateManagers.loginState import LoginState


class Screen(pygame.Surface):
    LOGIN = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guiRenderer = GuiRenderer(self)
        self.states = {self.LOGIN:LoginState(self)}

        self.last_pressed = pygame.key.get_pressed()
        self.last_clicked = pygame.mouse.get_pressed()

        self.__state = -1
        self.setState(self.LOGIN)

    def setState(self, value):
        self.__state = value
        self.states[self.__state].on_change()

    def update(self, dt, keysPressed, mouseClick, mousePos):
        self.fill((255, 255, 255))
        self.states[self.__state].during_screen(dt)
        self.guiRenderer.tick(dt, mousePos, mouseClick, self.last_clicked, keysPressed, self.last_pressed)
        self.last_pressed = keysPressed
        self.last_clicked = mouseClick
        self.guiRenderer.render(self)
