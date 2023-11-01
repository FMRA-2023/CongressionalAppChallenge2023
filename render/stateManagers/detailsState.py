import io

import pygame.transform

from colors import GRAY, WHITE, LIGHT_GREEN
from consts import NOTCH_SIZE, SIZE
from render.gui.base.font import RobotoSlab
from render.gui.elements.image import Image
from render.gui.elements.textElement import TextElement
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab
import requests


class DetailsState(StateManager):
    def __init__(self, app):
        super().__init__(app)
        self.event = None
        self.alreadyIn = []
        self.returnScreen = app.MAP
        self.ticket = ""

    def on_change(self):
        # print(self.returnScreen)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(SubmitButton(12, NOTCH_SIZE+10, "< Back", lambda:self.screen.setState(self.returnScreen)))
        guiRenderer.add_element(Image(12, NOTCH_SIZE+30, pygame.transform.scale(pygame.image.load(io.BytesIO(requests.get(self.event.featuredImage).content)), size=(SIZE[0]-24, SIZE[0]-24))))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+26, self.event.eventName, RobotoSlab.retrieve("bold", 28), WHITE))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+60, f"Company: {self.event.company}", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+80, f"Location: {self.event.address}", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+100, f"Exp needed: {self.event.experienceNeeded}", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+120, f"Age range: {self.event.minimumAge}-{self.event.maximumAge}", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(TextElement(12, NOTCH_SIZE+SIZE[0]+140, f"Description: {self.event.description}", RobotoSlab.retrieve("regular", 14), WHITE), tag="desc")

        guiRenderer.add_element(SubmitButton(12, guiRenderer.get_element("desc").y+guiRenderer.get_element("desc").h+20, "Sign Up", lambda:None), tag="signup")


        create_bottom_tab(self.screen)

    def signupEvent(self):
        self.screen.networking.signupEvent(self.event.eventName, self.screen.playerManager.myPlayer.id)
        self.screen.playerManager.myPlayer.points += 10
    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        signup = guiRenderer.get_element("signup")
        if self.ticket in self.screen.networking.responses.keys():
            self.alreadyIn = self.screen.networking.responses[self.ticket]["data"]
            self.ticket = self.screen.networking.getEventUsers(self.event.eventName)

        if self.ticket == "":
            self.ticket = self.screen.networking.getEventUsers(self.event.eventName)

        if self.screen.playerManager.myPlayer.id in self.alreadyIn:
            signup.on_release = lambda:None
            signup.renderables[0].color = GRAY
            signup.renderables[1].text.set_text("Signed Up")

        else:
            signup.on_release = self.signupEvent
            signup.renderables[0].color = LIGHT_GREEN
            signup.renderables[1].text.set_text("Sign Up")
        guiRenderer.render(self.screen)