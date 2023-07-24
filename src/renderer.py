import pygame
from pygame import Surface
from pygame.draw import lines, circle, line

from src.texture_library import TextureLibrary
from walls import Walls


class Renderer:
    wall_color = (50, 50, 255)

    def __init__(self, surface: Surface, walls: Walls, x, y, texture_library: TextureLibrary):
        self.texture_library = texture_library
        self.surface = surface
        self.x = x
        self.y = y
        self.x_center = x/2
        self.y_center = y/2
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

    def render_skeleton(self, distance):
        color = (255, 255, 255)
        width = 50.0
        size = 0
        if distance == 0:
            size = 3
        elif distance == 1:
            size = 2
        elif distance == 2:
            size = 1

        circle(self.surface, color, (self.x_center, self.y_center), width * size, 1)

    def render_texture(self, texture_name, distance):
        texture = self.get_texture(texture_name, self.x * 0.35 / (distance + 1))
        self.surface.blit(texture, (self.x_center - (texture.get_width() / 2),
                                    self.y_center - (texture.get_height() / 2)))

    def get_texture(self, texture_name, height):
        if texture_name == "skeleton_soldier":
            width = height
            texture = Surface((height, height), flags=pygame.SRCALPHA)
            white = (255, 255, 255)
            parts = self.texture_library.skeleton_soldier()
            for part in parts:
                lines(texture, white, False, [(point[0] * width, point[1] * height) for point in part])
            sword_parts = self.texture_library.short_sword_45()

            rusty = (94, 42, 22)
            size = height
            for sword_part in sword_parts:
                lines(texture, rusty, False, [(point[0] * size, point[1] * size) for point in sword_part])
            return texture
