from abc import ABC


class Component(ABC):
    def __init__(self, parent):
        self.id = self.__class__.__name__
        self._parent = parent
