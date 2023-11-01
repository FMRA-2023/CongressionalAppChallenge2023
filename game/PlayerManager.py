import math

import geocoder
import pygame

from consts import SIZE, LON_DIF, LAT_DIF
from game.player import Player
from render.gui.PlayerIcon import PlayerIcon


class PlayerManager:
    def __init__(self):
        self.players = {}
        self.myPlayer = None
        self.renders = set()

        self.nTicket = ""

    def update_renders(self, guiRenderer):
        for id in self.players.keys():
            self.renders.add(id)
        removes = set()
        for id in self.renders:
            if id not in self.players.keys():
                removes.add(id)
        self.renders.difference_update(removes)
        for id in self.renders:
            if not guiRenderer.has_element(f"player-{id}"):
                guiRenderer.add_element(PlayerIcon(id), tag=f"player-{id}")

            renderTo = pygame.Surface((100, 100), flags=pygame.SRCALPHA)
            self.players[id].render(renderTo, 50, 50)
            mapObj = guiRenderer.get_element('map')
            x = (self.players[id].long-mapObj.long)*math.cos(math.radians(mapObj.lat))*SIZE[0]/LON_DIF+SIZE[0]/2
            y = -(self.players[id].lat-mapObj.lat)*SIZE[1]/LAT_DIF+SIZE[1]/2
            guiRenderer.get_element(f"player-{id}").update(x-50, y-50, renderTo)

    def make_request(self, networking):
        self.nTicket = networking.update_and_request_player(self.myPlayer.generateDict())
        networking.set_user_data(self.myPlayer.id, self.myPlayer.generateDict())

    def update_players(self, networking):
        if self.nTicket in networking.responses:
            resp = networking.responses[self.nTicket]
            myId = self.myPlayer.id
            myUsername = self.myPlayer.username
            myPoints = self.myPlayer.points
            self.players = {}
            prevPos = (self.myPlayer.long, self.myPlayer.lat)
            prevDir = self.myPlayer.dir
            prevSkin = self.myPlayer.skin
            prevName = self.myPlayer.name
            for key, value in resp["data"].items():
                self.players[key] = Player(value[0][0], value[0][1], key, "N/A", value[2], value[1], 0)
            self.myPlayer = self.players[myId]
            self.myPlayer.username = myUsername
            self.myPlayer.points = myPoints
            self.myPlayer.long, self.myPlayer.lat = prevPos
            self.myPlayer.dir = prevDir
            self.myPlayer.skin = prevSkin
            self.myPlayer.name = prevName

            self.make_request(networking)



