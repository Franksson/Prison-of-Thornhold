import pygame
from pygame.event import Event, EventType

from src.input.input_event import InputEvent
from typing import Callable


class InputHandler:

    def __init__(self):
        self.input_events = dict()
        self.input_events["walk_forward"] = InputEvent(pygame.K_w)
        self.input_events["turn_left"] = InputEvent(pygame.K_a)
        self.input_events["turn_right"] = InputEvent(pygame.K_d)

    def on_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            for e in self.input_events.values():
                e.on_event(event)

    def subscribe(self, action: str, func: Callable):
        if self.input_events[action]:
            self.input_events[action].subscribe(func)
