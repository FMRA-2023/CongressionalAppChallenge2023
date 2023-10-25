import geocoder
import pygame

from consts import SIZE
from render.gui.elements.image import Image
import requests
import io

class Map(Image):
    def __init__(self, x, y, w, h):
        self.map = pygame.Surface((w, h))
        self.map.fill((255, 255, 255))
        super(Map, self).__init__(x, y, self.map)
        self.long, self.lat = geocoder.ip("me").latlng
        self.update_map()

        self.prevMouse = pygame.mouse.get_pos()

    def update_map(self):
        self.long +=0.001
        resp = requests.get(f"https://api.mapbox.com/styles/v1/ranne1234/clo4syurj00gn01p6hvwi1fn3/static/{self.lat}, {self.long},13,0,0/{SIZE[0]}x{SIZE[1]}?access_token=pk.eyJ1IjoicmFubmUxMjM0IiwiYSI6ImNsbzRuZ3gxaTAzMTQyaXQ4czFneXg1ZmsifQ.-3pbqKeJSvRaDFQQEctpBQ")
        img = pygame.image.load(io.BytesIO(resp.content))
        self.map.blit(img, (0, 0))

    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        self.update_map()