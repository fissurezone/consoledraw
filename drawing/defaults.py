# Global defaults for package drawing

DEFAULT_COLOUR = "x"
DEFAULT_EMPTY = " "


class DrawingError(Exception):
    pass


class LineTypeError(DrawingError):
    pass


class RectangleTypeError(DrawingError):
    pass
