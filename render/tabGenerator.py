from consts import SIZE
from render.gui.screenTab import ScreenTab


def create_bottom_tab(app):
    guiRenderer = app.guiRenderer
    guiRenderer.add_element(ScreenTab(0, 1, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*1/4, 3, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*1/2, 8, app))
    guiRenderer.add_element(ScreenTab(SIZE[0]*3/4, 7, app))