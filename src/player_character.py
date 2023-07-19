from src.debug_screen import DebugScreen
from enum import IntEnum

class Direction(IntEnum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class PlayerCharacter:

    def __init__(self, x: int, y: int, debug_screen: DebugScreen):
        self.x = x
        self.y = y
        self.facing = Direction.EAST
        self.debug_pos_text = debug_screen.init_row()
        self.debug_dir_text = debug_screen.init_row()
        self.debug_text_update()

    def debug_text_update(self):
        self.debug_pos_text.set("X: {x}, Y: {y}".format(x=self.x, y=self.y))
        self.debug_dir_text.set("Direction: {}".format(self.facing))

    def face(self, direction: Direction):
        self.facing = direction
        self.debug_text_update()

    def turn(self, clockwise=True):
        value = -1
        if clockwise:
            value = 1
        self.facing = ((self.facing + value) % 4)
        self.debug_text_update()

    def move_forward(self):
        if self.facing == Direction.NORTH:
            self.y -= 1
        elif self.facing == Direction.SOUTH:
            self.y += 1
        elif self.facing == Direction.EAST:
            self.x += 1
        elif self.facing == Direction.WEST:
            self.x -= 1
        self.debug_text_update()
