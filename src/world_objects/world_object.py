from abc import ABC
from src.components.component import Component


class WorldObject:
    def __init__(self):
        self.components = dict()

    def add_component(self, component: Component):
        self.components[component.id] = component

    def get_component(self, component_name: str):
        if component_name in self.components:
            return self.components[component_name]
        else:
            return None