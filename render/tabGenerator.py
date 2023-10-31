from consts import SIZE
from render.gui.screenTab import ScreenTab
from render.gui.eventsTab import EventsTab


def create_bottom_tab(app):
    guiRenderer = app.guiRenderer
    guiRenderer.add_element(ScreenTab(0, 1, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*1/4, 3, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*1/2, 8, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*3/4, 7, app))

def create_events_tab(app):
    guiRenderer = app.guiRenderer
    availableTab = EventsTab(0, 3, app, "Available")
    availableTab.textObj.centerAt((SIZE[0] / 3) / 2, 35)
    guiRenderer.add_element(availableTab) # Available
    createdEventsTab = EventsTab(SIZE[0] * 1/3, 9, app, "Created")
    createdEventsTab.textObj.centerAt(SIZE[0] / 2, 35)
    guiRenderer.add_element(createdEventsTab) # Created
    registeredEventsTab = EventsTab(SIZE[0] * 2/3, 10, app, "Registered")
    registeredEventsTab.textObj.centerAt(SIZE[0] * 5/6, 35)
    guiRenderer.add_element(registeredEventsTab) # Signed up
