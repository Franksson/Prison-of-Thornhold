class IntVector2D:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def turn_clockwise(self, times: int = 1):
        if times == 1:
            return IntVector2D(-self.y, self.x)
        elif times == 2:
            return IntVector2D(-self.x, -self.y)
        elif times == 3:
            return IntVector2D(self.y, -self.x)

    def __add__(self, other):
        return IntVector2D(self.x + other.x, self.y + other.y)
