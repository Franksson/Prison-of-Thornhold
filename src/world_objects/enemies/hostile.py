from abc import ABC, abstractmethod
from src.world_objects.world_object import WorldObject


class Hostile(ABC, WorldObject):
    def __init__(self, hitpoints=100):
        super().__init__()
        self.hitpoints = hitpoints
        