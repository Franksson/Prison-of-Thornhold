from pygame import Surface, draw, Rect
from UI.compass import Compass
from src.UI.anchor_point import AnchorPoint
from src.UI.ui_control import UIControl
from src.player_character import PlayerCharacter


class HeadsUpDisplay:
    def __init__(self, surface: Surface, width, height, player: PlayerCharacter):
        self.width = width
        self.height = height
        self.surface = surface
        self.controls: list[UIControl] = list()

        # Add UI controls
        self.controls.append(Compass(AnchorPoint.BottomCenter, self.width/2, self.height - 20, 100, 75, player))

    def draw(self):
        for control in self.controls:
            control.draw(self.surface)
