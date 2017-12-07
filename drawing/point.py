from defaults import *
from canvas import set_colour


def point(canvas, x, y, colour=DEFAULT_COLOUR):
    """
    Creates a point on the canvas

    :param canvas: canvas to manipulate
    :param x: x co-ordinate
    :param y: y co-ordinate
    :param colour: colour to set at the point
    :return: None
    """
    # points are 1 based co-ordinates increasing downwards and to the right from origin at top left (1,1)
    set_colour(canvas, x, y, colour)
