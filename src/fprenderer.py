from pygame.draw import lines
from walls import Walls


class Renderer:
    wall_color = (50, 50, 255)

    def __init__(self, surface, x, y):
        self.surface = surface
        self.walls = Walls(x, y)

    def draw_wall(self, wall):
        lines(self.surface, (50, 50, 255), True, wall)

    def render_walls(self, left: bool, right: bool, left_forward: bool, right_forward: bool, forward: bool):
        if left:
            self.draw_wall(self.walls.first_wall_l)
        else:
            self.draw_wall(self.walls.open_first_wall_l)
        if right:
            self.draw_wall(self.walls.first_wall_r)
        else:
            self.draw_wall(self.walls.open_first_wall_r)
        if left_forward:
            self.draw_wall(self.walls.second_wall_l)
        else:
            self.draw_wall(self.walls.open_second_wall_l)
        if right_forward:
            self.draw_wall(self.walls.second_wall_r)
        else:
            self.draw_wall(self.walls.open_second_wall_r)
        if forward:
            self.draw_wall(self.walls.end_wall)
