from src.components.component import Component
from src.int_vector_2d import IntVector2D
from src.world_objects.world_object import WorldObject


class WorldPositionComponent(Component):
    def __init__(self, worldmap, parent, blocks_player: bool = True):
        super().__init__(parent)
        self.position: IntVector2D = IntVector2D(0, 0)
        self._worldmap = worldmap
        self.blocks_player: bool = blocks_player

    def get_parent(self) -> WorldObject:
        return self._parent

    def set_position(self, x: int | IntVector2D, y: int = None):
        if y is not None and x is int:
            self.position.x = x
            self.position.y = y
        elif x is IntVector2D:
            self.position.x = x.x
            self.position.y = x.y

