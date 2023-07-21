from abc import ABC, abstractmethod

from src.UI.anchor_point import AnchorPoint


class UIControl(ABC):

    def __init__(self, anchor: AnchorPoint, left, top, width, height):
        self.anchor = anchor
        if anchor == AnchorPoint.TopLeft:
            self.left = left
            self.top = top
        elif anchor == AnchorPoint.TopCenter:
            self.left = left - (width/2)
            self.top = top
        elif anchor == AnchorPoint.TopRight:
            self.left = left - width
            self.top = top
        elif anchor == AnchorPoint.CenterLeft:
            self.left = left
            self.top = top - (height/2)
        elif anchor == AnchorPoint.CenterCenter:
            self.left = left - (width/2)
            self.top = top - (height/2)
        elif anchor == AnchorPoint.CenterRight:
            self.left = left - width
            self.top = top - (height/2)
        elif anchor == AnchorPoint.BottomLeft:
            self.left = left
            self.top = top - height
        elif anchor == AnchorPoint.BottomCenter:
            self.left = left - (width/2)
            self.top = top - height
        elif anchor == AnchorPoint.BottomRight:
            self.left = left - width
            self.top = top - height
        self.width = width
        self.height = height

    @abstractmethod
    def draw(self, surface):
        pass