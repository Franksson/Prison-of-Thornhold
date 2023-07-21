from pygame import Surface
from pygame.draw import lines
from walls import Walls


class Renderer:
    wall_color = (50, 50, 255)

    def __init__(self, surface: Surface, walls: Walls):
        self.surface = surface
        self.walls = walls

    @staticmethod
    def draw_wall(wall, surface: Surface):
        lines(surface, (50, 50, 255), True, wall)

    def render_walls(self,
                     left: bool, right: bool,
                     left_forward: bool, right_forward: bool,
                     forward: bool, second_forward: bool):
        if left:
            self.draw_wall(self.walls.first_wall_l, self.surface)
        else:
            self.draw_wall(self.walls.open_first_wall_l, self.surface)
        if right:
            self.draw_wall(self.walls.first_wall_r, self.surface)
        else:
            self.draw_wall(self.walls.open_first_wall_r, self.surface)
        if forward:
            self.draw_wall(self.walls.forward_wall, self.surface)
        else:
            if left_forward:
                self.draw_wall(self.walls.second_wall_l, self.surface)
            else:
                self.draw_wall(self.walls.open_second_wall_l, self.surface)
            if right_forward:
                self.draw_wall(self.walls.second_wall_r, self.surface)
            else:
                self.draw_wall(self.walls.open_second_wall_r, self.surface)
            if second_forward:
                self.draw_wall(self.walls.end_wall, self.surface)
