import io

import pygame
import requests

import loader
from colors import VERY_DARK_GREEN
from render.gui.base.font import RobotoSlab
from render.gui.base.element import GuiElement
from render.gui.base.renderable import Renderable
from render.gui.base.text import Text
from consts import SIZE


class EventCard(GuiElement):

    def __init__(self, x, y, width, height, event):
        
        # Create and add renderables
        renderables = []
        # Create background of card
        background = Renderable(pygame.Rect(0, y, SIZE[0], height), VERY_DARK_GREEN, 0)
        renderables.append(background)
        # Add image to event card
        renderables.append(Renderable(pygame.transform.scale(pygame.image.load(io.BytesIO(requests.get(event.featuredImage).content)), size=(0.37*width, 0.37*width)), (x + 0.12 * width, y + 0.125 * height)))
        #Add event name to event card
        eventNameObj = Text("Event name: " + event.eventName, RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x + 0.5 * width, y + 0.15 * height))
        companyObj = Text("Company: " + event.company, RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x + 0.5 * width, y + 0.35 * height))
        addressObj = Text("Address: " + event.address.split(',')[0], RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x + 0.5 * width, y + 0.55 * height))
        ageObj = Text("Ages: " + str(event.minimumAge) + "-" + str(event.maximumAge), RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x + 0.5 * width, y + 0.75 * height))
        textObjs = [eventNameObj, companyObj, addressObj, ageObj]
        for obj in textObjs:
            renderables.append(Renderable(obj))
        super(EventCard, self).__init__(x, y, renderables)
        self.width = width
        self.height = height
        self.event = event













    
    
    