from typing import Callable

from pygame.event import Event


class InputEvent:
    def __init__(self, key):
        self.key = key
        self.callables: list[Callable] = list()

    def on_event(self, event: Event):
        if event.key == self.key:
            self.send()

    def send(self):
        for func in self.callables:
            func()

    def subscribe(self, func: Callable):
        self.callables.append(func)