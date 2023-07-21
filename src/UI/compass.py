from pygame import Rect
from pygame.draw import ellipse, line, lines

from src.UI.anchor_point import AnchorPoint
from src.UI.ui_control import UIControl
from src.direction_enum import Direction
from src.player_character import PlayerCharacter


class Compass(UIControl):

    def __init__(self, anchor: AnchorPoint, left, top, width, height, player: PlayerCharacter):
        super().__init__(anchor, left, top, width, height)
        self.color = (150, 20, 20)
        self.line_thickness = 1
        self.pointing_to = player.facing
        player.subscribe(self)

    def update_direction(self, direction: Direction):
        self.pointing_to = direction

    def draw(self, surface):
        rect = Rect(self.left, self.top, self.width, self.height)
        ellipse(surface, self.color, rect, self.line_thickness)
        self.draw_line(surface)

    def on_event(self, context):
        if context["name"] == "player_direction":
            self.update_direction(context["value"])

    def draw_line(self, surface):
        line_start_pos = (
            self.left + (self.width / 2),
            self.top + (self.height / 2)
        )
        if self.pointing_to == Direction.NORTH:
            line_end_pos = (
                self.left + (self.width / 2),
                self.top
            )
        elif self.pointing_to == Direction.WEST:
            line_end_pos = (
                self.left + self.width,
                self.top + (self.height / 2)
            )
        elif self.pointing_to == Direction.SOUTH:
            line_end_pos = (
                self.left + (self.width / 2),
                self.top + self.height
            )
        elif self.pointing_to == Direction.EAST:
            line_end_pos = (
                self.left,
                self.top + (self.height / 2)
            )
        line(surface, self.color, line_start_pos, line_end_pos, self.line_thickness)
