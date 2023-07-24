from pygame import Surface


def mirror_horizontally(coordinates, width):
    return width - coordinates[0], coordinates[1]


def set_scale(parts, scale):
    return [[(point[0] * scale, point[1] * scale) for point in points] for points in parts]

def move_x_center(point: tuple[float, float], old: float, width: float):
    diff = (width / 2) - old
    return point[0] + diff, point[1]


class TextureLibrary:
    def skeleton_soldier(self):
        scale = 1/10
        left_side = {
            "head_l": [(5, 1), (4.5, 1), (4, 2), (4, 2.5), (4.5, 2.5), (4.5, 3), (5, 3)],
            "rib1_l": [(5, 3.5), (4, 4), (5, 4)],
            "rib2_l": [(5, 4), (4, 4.5), (5, 4.5)],
            "rib3_l": [(5, 4.5), (4.5, 5), (5, 5)],
            "collar_l": [(5, 3.5), (4, 3.5)],
            "hip_l": [(5, 6), (4.5, 5.5), (4.5, 6), (4.75, 6.5), (5, 6.5)],
            "leg_l": [(4.5, 6), (4, 8), (4.5, 9.5), (4, 10)]
        }
        right_side = [[mirror_horizontally(point, 10) for point in points] for points in left_side.values()]
        spine = [(5, 3), (5, 6)]
        arm_r = [(6, 3.5), (6.5, 5), (6, 6)]
        arm_l = [(4, 3.5), (3.75, 5.5), (3.5, 6.5)]
        everything = [spine, arm_l, arm_r] + right_side + list(left_side.values())
        return set_scale(everything, scale)

    def short_sword(self):
        scale = 1/8
        handle = [(1.5, 8), (1.5, 6)]
        guard = [(0, 6), (3, 6)]
        blade = [(1, 6), (1, 1), (1.5, 0), (2, 1), (2, 6)]
        parts = [handle, guard, blade]
        # parts = [[move_x_center(point, 1.5, 8) for point in part] for part in parts]
        return set_scale(parts, scale)

    def short_sword_45(self):
        scale = 1/10
        handle = [(4, 6), (3.5, 6.5)]
        guard = [(3, 6), (4, 7)]
        blade = [(3.25, 6.25), (2, 7.5), (2, 8), (2.5, 8), (3.75, 6.75)]
        parts = [handle, guard, blade]
        # parts = [[move_x_center(point, 1.5, 8) for point in part] for part in parts]
        return set_scale(parts, scale)
