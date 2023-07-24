from src.world_objects.enemies.hostile import Hostile
from src.int_vector_2d import IntVector2D
from src.components.world_position_component import WorldPositionComponent
from src.components.graphics_component import GraphicsComponent

class SkeletonSoldier(Hostile):
    def __init__(self, world, hitpoints=50):
        super().__init__(hitpoints)
        self.position: IntVector2D = IntVector2D()
        self.damage = 20
        self.target: 'PlayerCharacter' | None = None
        self.add_component(WorldPositionComponent(world, self))
        self.add_component(GraphicsComponent(self, "skeleton_soldier"))

    def set_target(self, target: 'PlayerCharacter'):
        self.target = target

    def attack(self):
        self.target.take_damage(self.damage)

    def take_turn(self):
        self.attack()
