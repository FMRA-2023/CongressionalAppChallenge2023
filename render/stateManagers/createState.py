# event name
# company
# description
# address
# experience needed
# minimum age
# maximum age
# featured image
from colors import GRAY, WHITE
from consts import SIZE
from render.gui.base.font import RobotoSlab
from render.gui.elements.textElement import TextElement
from render.gui.lTextInput import LongTextInput
from render.gui.sTextInput import STextInput
from render.gui.submitButton import SubmitButton
from render.stateManagers.StateManager import StateManager
from render.tabGenerator import create_bottom_tab


class CreateState(StateManager):
    def __init__(self, app):
        super().__init__(app)
        self.creating = False
        self.ticket = ""

    def on_change(self):
        guiRenderer = self.screen.guiRenderer
        guiRenderer.clear_elements()

        guiRenderer.add_element(TextElement(12, 30, "Create New Event", RobotoSlab.retrieve("bold", 30), WHITE))
        guiRenderer.add_element(TextElement(12, 80, "Name", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 100), tag="nameInput")

        guiRenderer.add_element(TextElement(12, 120, "Company", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 140), tag="companyInput")

        guiRenderer.add_element(TextElement(12, 160, "Experience Needed", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 180), tag="expInput")

        guiRenderer.add_element(TextElement(12, 200, "Age Range ([min] [max])", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 220), tag="ageInput")

        guiRenderer.add_element(TextElement(12, 240, "Link to Image", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(STextInput(12, 260), tag="linkInput")

        guiRenderer.add_element(TextElement(12, 280, "Address", RobotoSlab.retrieve("regular", 14), WHITE))
        guiRenderer.add_element(LongTextInput(12, 300, SIZE[0]-24), tag="addressInput")

        guiRenderer.add_element(TextElement(12, 320, "Description", RobotoSlab.retrieve("regular", 14), WHITE), tag="desc")
        guiRenderer.add_element(LongTextInput(12, 340, SIZE[0]-24), tag="descriptionInput")

        guiRenderer.add_element(SubmitButton(12, 360, "Create!", self.create_event), tag="createButton")

        create_bottom_tab(self.screen)

    def create_event(self):
        guiRenderer = self.screen.guiRenderer
        if guiRenderer.has_element("warning"):
            guiRenderer.remove_element("warning")
        good = True
        # print([guiRenderer.get_element(f"{i}Input").text for i in ["name", "company", "address", "exp", "age", "link", "description"]])
        if "" in [guiRenderer.get_element(f"{i}Input").text for i in ["name", "company", "address", "exp", "age", "link", "description"]]:
            good = False

        try:
            [int(i) for i in guiRenderer.get_element("ageInput").text.split()]

        except ValueError:
            good = False

        if not good:
            guiRenderer.add_element(TextElement(SIZE[0]/2, guiRenderer.get_element("createButton").y, "Invalid field",
                                                RobotoSlab.retrieve("regular", 14), (255, 0, 0)), tag="warning")

        else:
            guiRenderer.add_element(TextElement(SIZE[0]/2, guiRenderer.get_element("createButton").y, "Signing Up...",
                                                RobotoSlab.retrieve("regular", 14), (0, 255, 0)), tag="warning")
            self.ticket = self.screen.networking.create_event({"name":guiRenderer.get_element(f"nameInput").text,
                                                 "company":guiRenderer.get_element(f"companyInput").text,
                                                 "description":guiRenderer.get_element(f"descriptionInput").text,
                                                 "address":guiRenderer.get_element(f"addressInput").text,
                                                 "experienceNeeded":guiRenderer.get_element(f"expInput").text,
                                                 "featuredImage":guiRenderer.get_element(f"linkInput").text,
                                                 "minimumAge":int(guiRenderer.get_element(f"ageInput").text.split()[0]),
                                                 "maximumAge":int(guiRenderer.get_element(f"ageInput").text.split()[1])})
            self.creating = True


    def during_screen(self, dt):
        self.screen.fill(GRAY)
        guiRenderer = self.screen.guiRenderer
        if self.creating:
            if self.ticket in self.screen.networking.responses.keys():
                guiRenderer.get_element("warning").renderables[0].text.set_text("Success!")
        guiRenderer.render(self.screen)
        guiRenderer.get_element("desc").moveTo(12, 300+guiRenderer.get_element("addressInput").h+20)
        guiRenderer.get_element("descriptionInput").moveTo(12, guiRenderer.get_element("desc").y + 20)
        guiRenderer.get_element("createButton").moveTo(12, guiRenderer.get_element("descriptionInput").y+guiRenderer.get_element("descriptionInput").h+20)
        #print(guiRenderer.get_element("descriptionInput").y, guiRenderer.get_element("descriptionInput").h)
        #print(guiRenderer.get_element("descriptionInput").y+guiRenderer.get_element("descriptionInput").h+20)