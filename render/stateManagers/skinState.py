import pygame

from colors import GRAY, LIGHT_GRAY, WHITE
from consts import SIZE
from render.gui.SkinOption import SkinOption
from render.gui.base.element import GuiElement
from render.gui.base.font import RobotoSlab
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text
from render.gui.elements.image import Image
from render.gui.elements.textElement import TextElement
from render.gui.elements.textinput import TextInput
from render.gui.sTextInput import STextInput
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab


class SkinState(StateManager):
    def __init__(self, screen, player):
        super(SkinState, self).__init__(screen)
        self.player = player

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(Image(SIZE[0]/2-150/2, 300-105/2, pygame.Surface((150, 105), flags=pygame.SRCALPHA)), tag="playerPreview")

        guiRenderer.add_element(TextElement(50, 155, "Left", RobotoSlab.retrieve("regular", 24), WHITE, centerAt=True))
        for i in range(5):
            guiRenderer.add_element(SkinOption(30, 175+50*i, "left_hand", i, self.player))

        guiRenderer.add_element(TextElement(SIZE[0]-30-20, 155, "Right", RobotoSlab.retrieve("regular", 24), WHITE, centerAt=True))
        for i in range(5):
            guiRenderer.add_element(SkinOption(SIZE[0]-30-40, 175+50*i, "right_hand", i, self.player))

        guiRenderer.add_element(TextElement(SIZE[0]/2, 65, "Base", RobotoSlab.retrieve("regular", 24), WHITE, centerAt=True))
        for i in range(5):
            guiRenderer.add_element(SkinOption(SIZE[0]/2-100+50*i - 20, 90, "base", i, self.player))

        guiRenderer.add_element(TextElement(SIZE[0]/2, SIZE[1]/2+110, "Hair/Hat", RobotoSlab.retrieve("regular", 24), WHITE, centerAt=True))

        for i in range(5):
            guiRenderer.add_element(SkinOption(SIZE[0]/2-100+50*i - 20, SIZE[1]/2+130, "hat", i, self.player))

        guiRenderer.add_element(TextElement(30, SIZE[1]/2+190, "Display Name", RobotoSlab.retrieve("regular", 18), WHITE))
        guiRenderer.add_element(STextInput(30, SIZE[1]/2+215))
        create_bottom_tab(self.screen)

    def during_screen(self, dt):
        self.screen.fill(LIGHT_GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.get_element("playerPreview").renderables[0].disp.fill((0, 0, 0, 0))
        preDisp = pygame.Surface((50, 35), pygame.SRCALPHA)
        self.player.render(preDisp, 25, 18)
        guiRenderer.get_element("playerPreview").renderables[0].disp.blit(pygame.transform.scale(preDisp, (150, 105)), (0, 0))
        guiRenderer.render(self.screen)