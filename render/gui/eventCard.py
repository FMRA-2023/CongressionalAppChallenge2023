import pygame

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
        background = Renderable(pygame.Rect(x, y, width, height))
        renderables.append(background, VERY_DARK_GREEN, 0)
        # Add image to event card
        renderables.append(Renderable(pygame.transform.scale(loader.load_image("https://preview.redd.it/an871k4o1sn51.png?width=440&format=png&auto=webp&s=85dcd6cb73b8760802e254ee14dfa3c7ab444591"), size=(0.25 * width, 0.25 * height)), (x + 0.125 * width, y + 0.125 * height)))
        #Add event name to event card
        eventNameObj = Text("Event name: Hi", RobotoSlab.retrieve("regular", 12), (255, 255, 255), (x + 0.5 * width, y + 0.2 * height))


        super(EventCard, self).__init__(x, y, renderables)
        self.width = width
        self.height = height
        self.event = event













    
    
    