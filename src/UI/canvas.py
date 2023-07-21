from abc import ABC, abstractmethod
from src.UI.ui_control import UIControl


class Canvas(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.controls: list[UIControl] = list()

    @abstractmethod
    def draw(self):
        pass
