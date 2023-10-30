import math

import geocoder
import pygame

from consts import SIZE, LON_DIF, LAT_DIF
from game.player import Player
from render.gui.PlayerIcon import PlayerIcon


class PlayerManager:
    def __init__(self):
        self.players = {"frankliu":Player(0, 0, 0, "frankliu", "frank liu", {"base":0, "hat":1, "left_hand":3, "right_hand":4}),
                        "frankliu2":Player(-75.5138, 40.0362, 1, "frankliu2", "frank liu", {"base":0, "hat":1, "left_hand":3, "right_hand":4}),
                        "frankliu3":Player(-75.5238, 40.0362, 1, "frankliu2", "frank liu", {"base":0, "hat":1, "left_hand":3, "right_hand":4})}
        self.myPlayer = self.players["frankliu"]
        self.myPlayer.lat, self.myPlayer.long = geocoder.ip("me").latlng
        self.renders = set()

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

            renderTo = pygame.Surface((70, 70), flags=pygame.SRCALPHA)
            self.players[id].render(renderTo, 35, 35)
            mapObj = guiRenderer.get_element('map')
            x = (self.players[id].long-mapObj.long)*math.cos(math.radians(mapObj.lat))*SIZE[0]/LON_DIF+SIZE[0]/2
            y = -(self.players[id].lat-mapObj.lat)*SIZE[1]/LAT_DIF+SIZE[1]/2
            guiRenderer.get_element(f"player-{id}").update(x-35, y-35, renderTo)

