import pygame

import loader
from colors import GRAY, WHITE, LIGHT_GRAY
from consts import SIZE
from render.gui.base.font import RobotoSlab
from render.gui.base.text import Text
from render.gui.elements.image import Image
from render.gui.elements.textElement import TextElement
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab


class ProfileState(StateManager):
    def __init__(self, app):
        super().__init__(app)

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        renderTo = pygame.Surface((50, 35), pygame.SRCALPHA)
        self.screen.playerManager.myPlayer.render(renderTo, 25, 18)
        guiRenderer.add_element(Image(12, 50, pygame.transform.scale(renderTo, (SIZE[0]-24, (SIZE[0]-24)*0.7))))
        guiRenderer.add_element(SubmitButton(SIZE[0]-125, SIZE[1]-95, "Edit Skin", lambda:self.screen.setState(self.screen.SKIN)))
        guiRenderer.add_element(TextElement(12, 50+(SIZE[0]-24)*0.7+10, self.screen.playerManager.myPlayer.name, RobotoSlab.retrieve("bold", 32), WHITE))
        guiRenderer.add_element(TextElement(12, 50+(SIZE[0]-24)*0.7+45, f"@{self.screen.playerManager.myPlayer.username}", RobotoSlab.retrieve("regular", 18), WHITE))
        guiRenderer.add_element(TextElement(12, 50+(SIZE[0]-24)*0.7+70, f"UID: {self.screen.playerManager.myPlayer.id}", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(Image(12, 50+(SIZE[0]-24)*0.7+100, loader.load_image("points", size=(100, 100))))
        guiRenderer.add_element(TextElement(12+100+Text(f"{self.screen.playerManager.myPlayer.points}", RobotoSlab.retrieve("bold", 48), (0, 0, 0), (0, 0)).w/2, 50+(SIZE[0]-24)*0.7+150, f"{self.screen.playerManager.myPlayer.points}", RobotoSlab.retrieve("bold", 48), WHITE, centerAt=True))

        create_bottom_tab(self.screen)

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)