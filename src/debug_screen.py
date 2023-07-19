from pygame.font import SysFont
from pygame import Surface


class DebugRow:
    def __init__(self):
        self.text = ""

    def set(self, text):
        self.text = text


class DebugScreen:
    def __init__(self):
        self.debug_font = SysFont("consolas", 22)
        self.rows: [DebugRow] = []

    def init_row(self):
        row = DebugRow()
        self.rows.append(row)
        return row

    def render(self, surface: Surface):
        height = 0
        color = (255, 255, 255)
        for row in self.rows:
            surface.blit(
                self.debug_font.render(row.text, False, color),
                (0, height))
            height = height + self.debug_font.get_height()
