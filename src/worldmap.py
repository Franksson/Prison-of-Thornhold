from int_vector_2d import IntVector2D as Vector2
from src.components.world_position_component import WorldPositionComponent
from src.world_objects.enemies.skeleton_soldier import SkeletonSoldier

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
        self.world: dict[tuple[int, int]: list[WorldPositionComponent]] = dict()

        skeleton = SkeletonSoldier(self)
        self.add(skeleton.get_component("WorldPositionComponent"), 5, 5)

    def add(self, worldPositionComponent: WorldPositionComponent, x, y):
        if (x, y) not in self.world:
            self.world[(x, y)] = list()
        self.world[(x, y)].append(worldPositionComponent)
        worldPositionComponent.set_position(x, y)

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

    def get_position(self, x, y):
        if (x, y) not in self.world:
            return None
        else:
            return self.world[(x, y)]

    def get_wall(self, vector2: Vector2):
        return self.world_map[vector2.y][vector2.x]

    def obstructed(self, vector: Vector2):
        obstacle = False
        pos = self.get_position(vector.x, vector.y)
        if pos is not None:
            for wpc in pos:
                if wpc.blocks_player:
                    obstacle = True
        return self.isWall(vector) or obstacle


