from src.components.component import Component


class GraphicsComponent(Component):
    def __init__(self, parent, texture_name: str):
        super().__init__(parent)
        self.texture_name = texture_name
