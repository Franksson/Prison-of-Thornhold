from src.components.world_position_component import WorldPositionComponent
from src.direction_enum import Direction
from src.renderer import Renderer
from src.int_vector_2d import IntVector2D


class FirstPersonCameraComponent:
    def __init__(self, parent, renderer: Renderer):
        self.parent = parent
        self.renderer = renderer

    def render_walls(self):
        if self.parent.world is None:
            return

        walls_pos: {str, IntVector2D} = {
            "left": IntVector2D(-1, 0),
            "right": IntVector2D(1, 0),
            "forward": IntVector2D(0, -1),
            "second_left": IntVector2D(-1, -1),
            "second_right": IntVector2D(1, -1),
            "second_forward": IntVector2D(0, -2),
        }
        if self.parent.facing == Direction.EAST:
            walls_pos = {key: value.turn_clockwise(1) for key, value in walls_pos.items()}
        elif self.parent.facing == Direction.SOUTH:
            walls_pos = {key: value.turn_clockwise(2) for key, value in walls_pos.items()}
        elif self.parent.facing == Direction.WEST:
            walls_pos = {key: value.turn_clockwise(3) for key, value in walls_pos.items()}

        left = self.check_if_wall(walls_pos["left"])
        right = self.check_if_wall(walls_pos["right"])
        forward = self.check_if_wall(walls_pos["forward"])
        second_left = self.check_if_wall(walls_pos["second_left"])
        second_right = self.check_if_wall(walls_pos["second_right"])
        second_forward = self.check_if_wall(walls_pos["second_forward"])

        self.renderer.render_walls(left, right, second_left, second_right, forward, second_forward)

    def check_if_wall(self, pos: IntVector2D):
        world_pos = IntVector2D(self.parent.x + pos.x, self.parent.y + pos.y)
        if self.parent.world is not None:
            return self.parent.world.isWall(world_pos)

    def get_world_objects_forward(self, distance: int = 0) -> list[WorldPositionComponent] | None:
        forward = IntVector2D(0, -1).turn_clockwise(self.parent.facing)
        forward = forward * (distance + 1)
        world_coords = IntVector2D(self.parent.x + forward.x, self.parent.y + forward.y)
        return self.parent.world.get_position(world_coords.x, world_coords.y)

    def render_forwards(self):
        for i in range(2):
            worldPositionComponents = self.get_world_objects_forward(i)
            if worldPositionComponents is not None:
                for component in worldPositionComponents:
                    texture = component.get_parent().get_component("GraphicsComponent").texture_name
                    self.renderer.render_texture(texture, i)
