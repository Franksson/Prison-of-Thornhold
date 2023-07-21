from pygame import Vector2

DEAD_END_HEIGHT = 0.2
DEAD_END_WIDTH = 0.2
FIRST_WALL_WIDTH = 0.40
SECOND_WALL_WIDTH = 0.60


class Walls:
    def __init__(self, x, y) -> None:
        # screen Vectors
        self.screen = Vector2(x, y)
        s_height = Vector2(0, y)

        # End wall dimensions
        end_width = int(x * DEAD_END_WIDTH)
        end_height = end_width
        end_left = x / 2 - end_width / 2
        end_top = y / 2 - end_height / 2

        # End wall points
        end_a = Vector2(end_left, end_top)
        end_b = s_height + Vector2(end_a.x, -end_a.y)
        end_points = [end_a, end_b]

        # First wall points
        wall_width = int(((x - end_width) / 2) * FIRST_WALL_WIDTH)
        wall_height = int(((y - end_height) / 2) * FIRST_WALL_WIDTH)
        wall_b = Vector2(wall_width, wall_height)
        wall_c = Vector2(wall_b.x, self.screen.y - wall_b.y)
        wall_points = [wall_b, wall_c]

        # Walls
        self.first_wall_l = [Vector2(0, 0), wall_b, wall_c, Vector2(0, y)]
        self.end_wall = end_points + [self.mirror(x) for x in end_points][::-1]
        self.forward_wall = wall_points + [self.mirror(points) for points in wall_points][::-1]
        self.second_wall_l = [wall_b, end_a, end_b, wall_c]
        self.open_first_wall_l = [Vector2(0, wall_b.y), wall_b, wall_c, Vector2(0, wall_c.y)]
        self.open_second_wall_l = [Vector2(wall_b.x, end_a.y), end_a, end_b, Vector2(wall_c.x, end_b.y)]

        # Right walls
        self.first_wall_r = [self.mirror(x) for x in self.first_wall_l]
        self.second_wall_r = [self.mirror(x) for x in self.second_wall_l]
        self.open_first_wall_r = [self.mirror(x) for x in self.open_first_wall_l]
        self.open_second_wall_r = [self.mirror(x) for x in self.open_second_wall_l]

    def mirror(self, vec):
        return Vector2(self.screen.x - vec.x, vec.y)