import math
import pygame
import consts
from consts import SIZE
from render.gui.elements.image import Image
import requests
import io
import threading

class Map(Image):
    LON_DIF = consts.LON_DIF
    LAT_DIF = consts.LAT_DIF

    def __init__(self, x, y, w, h, app):
        self.map = pygame.Surface((w, h))
        self.map.fill((255, 255, 255))
        super(Map, self).__init__(x, y, self.map)
        self.lat, self.long = app.playerManager.myPlayer.lat, app.playerManager.myPlayer.long
        self.currentMap = None
        self.currentBBox = None
        self.retrv = False
        self.request(self.long, self.lat)
        self.update_map()
        self.doubleClickTime = 0
        self.app = app

        self.original = (self.long, self.lat)
        self.dest = (self.long, self.lat)
        self.timeLeft = 0


    def get_bounding_box(self, long, lat):
        return [long-self.LON_DIF, lat-self.LAT_DIF, long+self.LON_DIF, lat+self.LAT_DIF]
        # return f"{self.long},{self.lat},13,0,0"

    def request(self, long, lat):
        if self.retrv:
            return
        self.retrv = True
        bbox = self.get_bounding_box(long, lat)
        resp = requests.get(f"https://api.mapbox.com/styles/v1/ranne1234/clo4syurj00gn01p6hvwi1fn3/static/{str(bbox).replace(' ', '')}/{SIZE[0]*2}x{SIZE[1]*2}?access_token=pk.eyJ1IjoicmFubmUxMjM0IiwiYSI6ImNsbzRuZ3gxaTAzMTQyaXQ4czFneXg1ZmsifQ.-3pbqKeJSvRaDFQQEctpBQ")
        img = pygame.image.load(io.BytesIO(resp.content))
        self.currentBBox = bbox
        self.currentMap = img
        self.retrv = False


    def update_map(self):
        if self.long+self.LON_DIF*5/8 > self.currentBBox[2] or self.long-self.LON_DIF*5/8 < self.currentBBox[0] \
            or self.lat + self.LAT_DIF*3/4 > self.currentBBox[3] or self.lat - self.LAT_DIF*3/4 < self.currentBBox[1]:
            threading.Thread(target=self.request, args=(self.long, self.lat,)).start()
        self.map.fill((255, 255, 255))
        self.map.blit(self.currentMap, ((self.currentBBox[0]-self.long)*math.cos(math.radians(self.lat))*SIZE[0]/self.LON_DIF+SIZE[0]/2,
                                        -(self.currentBBox[1]-self.lat)*SIZE[1]/self.LAT_DIF-3*SIZE[1]/2))
        pygame.draw.circle(self.map, (255, 0, 0), (SIZE[0]/2, SIZE[1]/2), 5)

    def disp_to_geo(self, x, y):
        renderX, renderY = ((self.currentBBox[0]-self.long)*math.cos(math.radians(self.lat))*SIZE[0]/self.LON_DIF+SIZE[0]/2,
        -(self.currentBBox[1]-self.lat)*SIZE[1]/self.LAT_DIF-3*SIZE[1]/2)

        return ((x-renderX)/(SIZE[0]*math.cos(math.radians(self.lat))) * self.LON_DIF + self.currentBBox[0], -(y-renderY)/SIZE[1] * self.LAT_DIF + self.currentBBox[3])


    def tick(self, dt, mousePos, mouseClicked, prevClicked, keys, prevKeys):
        self.long, self.lat = self.app.playerManager.myPlayer.long, self.app.playerManager.myPlayer.lat
        self.update_map()
        if not mouseClicked[0] and prevClicked[0]:
            self.doubleClickTime = 0.5

        self.doubleClickTime -= dt
        if self.doubleClickTime < 0:
            self.doubleClickTime = 0

        if mouseClicked[0] and self.doubleClickTime > 0:
            self.doubleClickTime = 0
            self.original = (self.long, self.lat)
            self.dest = self.disp_to_geo(*mousePos)
            self.timeLeft = 1

        if self.timeLeft > 0:
            self.timeLeft -= dt
            self.app.playerManager.myPlayer.long = self.original[0] * self.timeLeft + self.dest[0] * (1-self.timeLeft)
            self.app.playerManager.myPlayer.lat = self.original[1] * self.timeLeft + self.dest[1] * (1-self.timeLeft)
            self.app.playerManager.myPlayer.dir = math.degrees(math.atan2(self.dest[1]-self.original[1], self.dest[0]-self.original[0]))

        else:
            self.timeLeft = 0
            self.app.playerManager.myPlayer.long, self.app.playerManager.myPlayer.lat = self.dest
