from typing import Callable

from src.debug_screen import DebugScreen
from direction_enum import Direction
from components.fp_camera import FirstPersonCameraComponent
from renderer import Renderer
from src.input.input_handler import InputHandler
from src.worldmap import WorldMap
from int_vector_2d import IntVector2D


class PlayerCharacter:

    def __init__(self, x: int, y: int,
                 input_handler: InputHandler,
                 debug_screen: DebugScreen,
                 renderer: Renderer):
        self.x = x
        self.y = y
        self.facing = Direction.EAST
        self.debug_pos_text = debug_screen.init_row()
        self.debug_dir_text = debug_screen.init_row()
        self.debug_text_update()
        self.world: WorldMap | None = None
        self.camera: FirstPersonCameraComponent = FirstPersonCameraComponent(self, renderer)
        self.subscribers = list()

        # Map input
        input_handler.subscribe("walk_forward", self.move_forward)
        input_handler.subscribe("turn_left", self.turn_left)
        input_handler.subscribe("turn_right", self.turn_right)

    def send_event(self, context):
        # context = {"x": self.x, "y": self.y, "player_facing": self.facing}
        for sub in self.subscribers:
            sub.on_event(context)

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def set_world(self, world: WorldMap):
        self.world = world

    def debug_text_update(self):
        self.debug_pos_text.set("X: {x}, Y: {y}".format(x=self.x, y=self.y))
        self.debug_dir_text.set("Direction: {}".format(self.facing))

    def face(self, direction: Direction):
        self.facing = direction
        self.debug_text_update()

    def turn_right(self):
        self.turn()

    def turn_left(self):
        self.turn(False)

    def turn(self, clockwise=True):
        value = -1
        if clockwise:
            value = 1
        self.facing = ((self.facing + value) % 4)
        self.debug_text_update()
        context = {"name": "player_direction", "value": self.facing}
        self.send_event(context)

    def move_forward(self):
        move_vector = IntVector2D()
        if self.facing == Direction.NORTH:
            move_vector.y = -1
        elif self.facing == Direction.SOUTH:
            move_vector.y = 1
        elif self.facing == Direction.EAST:
            move_vector.x = 1
        elif self.facing == Direction.WEST:
            move_vector.x = -1

        new_pos = IntVector2D(self.x, self.y) + move_vector

        if self.can_move_to(new_pos):
            self.x = new_pos.x
            self.y = new_pos.y
            self.debug_text_update()

    def can_move_to(self, move_vector):
        result = False
        if self.world is not None:
            result = self.world.isWall(move_vector) is False
        return result
