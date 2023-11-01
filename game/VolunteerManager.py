import math
import time

from consts import SIZE, LON_DIF, LAT_DIF
from networking.VolunteerEvent import VolunteerEvent
from render.gui.eventMarker import EventMarker


class VolunteerManager:
    def __init__(self):
        self.events = []
        self.names = set()
        self.renders = set()
        self.ticket = ""
        self.timeSinceLastSent = time.time()-5

    def make_request(self, networking):
        self.ticket = networking.get_events_num(100)
        self.timeSinceLastSent = time.time()

    def updateVolunteers(self, networking):
        if time.time() - self.timeSinceLastSent > 5:
            if self.ticket in networking.responses.keys():
                netw = networking
                events = [VolunteerEvent(unFormattedEvent['Name'], unFormattedEvent['Company'], unFormattedEvent['Description'], unFormattedEvent['Full Address'], unFormattedEvent['Experience Needed'], unFormattedEvent['Minimum Age'], unFormattedEvent['Maximum Age'], unFormattedEvent['Featured Image']) for unFormattedEvent in netw.responses[self.ticket]['data']] # retrieve data
                for event in events:
                    if event not in self.names:
                        self.events.append(event)
                        self.names.add(f"{event.eventName}:{event.company}")
                self.make_request(networking)

    def updateRender(self, screen):
        guiRenderer = screen.guiRenderer
        for event in self.events:
            if not guiRenderer.has_element(f"icon-{event.eventName}:{event.company}"):
                guiRenderer.add_element(EventMarker(0, 0, event, screen), tag=f"icon-{event.eventName}:{event.company}")
            mapObj = guiRenderer.get_element('map')
            x = (event.longitude-mapObj.long)*math.cos(math.radians(mapObj.lat))*SIZE[0]/LON_DIF+SIZE[0]/2
            y = -(event.latitude-mapObj.lat)*SIZE[1]/LAT_DIF+SIZE[1]/2
            element = guiRenderer.get_element(f"icon-{event.eventName}:{event.company}")
            textObj = element.renderables[2].text
            element.moveTo(x-textObj.w/2-5, y-10-textObj.h/2-5)


