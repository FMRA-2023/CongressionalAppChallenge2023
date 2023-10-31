import pygame

import loader
from render.gui.base.font import RobotoSlab
from render.gui.base.text import Text


class Player:
    def __init__(self, long, lat, id, username, name, skin, points):
        self.long = long
        self.lat = lat
        self.id = id
        self.username = username
        self.name = name
        self.skin = skin
        self.dir = 0
        self.points = points

    # rotate around a set point (in most cases, center)
    def rotate(self, image, pos, originPos, angle): # Credit to Rabbid76 (https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame)

        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # rotated image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # return image
        return rotated_image, rotated_image_rect

    def render(self, screen, x, y):
        textObj = Text(self.name, RobotoSlab.retrieve("bold", 12), (255, 255, 255), (0, 0))
        renderTo = pygame.Surface((50, 50), flags=pygame.SRCALPHA)
        renderTo.blit(loader.load_image(f"skins/hand/{self.skin['left_hand']}"), (25-10-8, 15))
        renderTo.blit(pygame.transform.flip(loader.load_image(f"skins/hand/{self.skin['right_hand']}"), True, False), (25+10-1, 15))
        renderTo.blit(loader.load_image(f"skins/base/{self.skin['base']}"), (9, 9))
        renderTo.blit(loader.load_image(f"skins/hat/{self.skin['hat']}"), (9, 9))
        img, rect = self.rotate(renderTo, (x, y), (25, 25), self.dir-90)
        textObj.centerAt(x, y-25)
        textObj.render(screen)
        screen.blit(img, rect)

    def generateDict(self):
        return {"player_id":self.id, "pos":(self.long, self.lat), "skin":self.skin, "display_name":self.name, "dir":self.dir}
