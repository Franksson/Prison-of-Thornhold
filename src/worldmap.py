from int_vector_2d import IntVector2D as Vector2

class WorldMap:

    def __init__(self):
        self.player = None
        self.world_map = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def addPlayer(self, player):
        self.player = player

    def isWall(self, vector: Vector2):
        # if out of bounds return true
        # if 1 return false
        pass
        max_y = len(self.world_map)
        max_x = len(self.world_map[0])
        if vector.x >= max_x or vector.x < 0:
            return True
        if vector.y >= max_y or vector.x < 0:
            return True
        if self.get_wall(vector) == 1:
            return False
        else:
            return True

    def get_wall(self, vector2: Vector2):
        return self.world_map[vector2.y][vector2.x]



