from typing import Callable

from pygame import Rect


class Button:
    def __init__(self, left, top, width, height):
        self.rect = Rect(left, top, width, height)
        self.events: list[Callable] = list()

    def on_click(self):
        for event in self.events:
            event()

    def subscribe(self, func: Callable):
        self.events.append(func)
