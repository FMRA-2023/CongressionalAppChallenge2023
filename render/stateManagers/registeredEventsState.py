from colors import GRAY
from consts import NOTCH_SIZE, SIZE
from render.gui.base.font import RobotoSlab
from render.stateManagers.StateManager import StateManager
from render.gui.elements.textElement import TextElement
from render.tabGenerator import create_bottom_tab, create_events_tab
from networking.networking import Networking
from networking.VolunteerEvent import VolunteerEvent
from render.gui.eventCard import EventCard

class RegisteredEventsState(StateManager):
    def __init__(self, screen):
        super().__init__(screen)
    
    def on_change(self):
        netw = Networking()
        ticket = netw.getRegisteredEvents(5, "6541730a15f4babb040385ba") # netw is Networking object, send query data
        while ticket not in netw.responses: # wait until response is received
        # do something here like make a loading sign
            pass
        self.events = netw.responses[ticket]['data'] # retrieve data
        self.numEvents = len(self.events)

        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()
        guiRenderer.add_element(TextElement(10, NOTCH_SIZE + 15, "Registered Events", RobotoSlab.retrieve("bold", 25), (255, 255, 255)), tag="registeredTitle")

        for i in range(self.numEvents):
            unFormattedEvent = self.events[i]
            event = VolunteerEvent(unFormattedEvent['Name'], unFormattedEvent['Company'], unFormattedEvent['Description'], unFormattedEvent['Full Address'], unFormattedEvent['Experience Needed'], unFormattedEvent['Minimum Age'], unFormattedEvent['Maximum Age'], unFormattedEvent['Featured Image'])
            availableHeight = SIZE[1] * 0.5
            rectangleHeight = availableHeight / (self.numEvents + (self.numEvents - 1) * 0.05)
            eventCard = EventCard(0.1 * SIZE[0], 0.25 * SIZE[1] + (i * rectangleHeight * (1 + 0.05)), 0.5 * SIZE[0], rectangleHeight, event)
            guiRenderer.add_element(eventCard)
        
        create_bottom_tab(self.screen)
        create_events_tab(self.screen)
            

    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        guiRenderer.render(self.screen)
    