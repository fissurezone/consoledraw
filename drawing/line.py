from defaults import *
from canvas import is_x_in_canvas, is_y_in_canvas, contain_x_range_to_canvas, contain_y_range_to_canvas
from point import point


def vertical_line(canvas, x, start_y, end_y, colour=DEFAULT_COLOUR):
    """
    Creates a vertical line segment at column y of the canvas

    :param canvas: canvas to manipulate
    :param x: column to create line at
    :param start_y: starting row of line segment
    :param end_y: ending row of line segment
    :param colour: colour to set at line segment positions
    :return: None

    :Example:

    vertical_line(canvas(5,5), 1, 2, 4) == [[' ', ' ', ' ', ' ', ' '],
                                            ['x', ' ', ' ', ' ', ' '],
                                            ['x', ' ', ' ', ' ', ' '],
                                            ['x', ' ', ' ', ' ', ' '],
                                            [' ', ' ', ' ', ' ', ' ']]
    """
    if is_x_in_canvas(canvas, x):
        tup = (start_y, end_y)
        # since we want a range, we determine min and max of tuple
        range_tup = (min(*tup), max(*tup))
        for y in contain_y_range_to_canvas(canvas, *range_tup):
            point(canvas, x, y, colour)


def horizontal_line(canvas, y, start_x, end_x, colour=DEFAULT_COLOUR):
    """
    Creates a horizontal line segment at row x of the canvas

    :param canvas: canvas to manipulate
    :param y: row to create line at
    :param start_x: starting column of line segment
    :param end_x: ending column of line segment
    :param colour: colour t set at line segment positions
    :return: None

    :Example:

    horizontal_line(canvas(5,5), 1, 2, 4) == [[' ', 'x', 'x', 'x', ' '],
                                              [' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ', ' ']]
    """
    if is_y_in_canvas(canvas, y):
        tup = (start_x, end_x)
        # since we want a range, we determine min and max of tuple
        range_tup = (min(*tup), max(*tup))
        for x in contain_x_range_to_canvas(canvas, *range_tup):
            point(canvas, x, y, colour)


def line(canvas, start_x, start_y, end_x, end_y, colour=DEFAULT_COLOUR):
    """
    Creates vertical or horizontal line segment

    :param canvas: canvas to manipulate
    :param start_x: x co-ordinate of starting position
    :param start_y: y co-ordinate of starting position
    :param end_x: x co-ordinate of ending position
    :param end_y: y co-ordinate of ending position
    :param colour: colour ro set at line segment positions
    :return: None
    :raises LineTypeError: when line segment is neither vertical nor horizontal
    """
    # function expects straight horizontal or vertical line segments
    try:
        assert (start_x == end_x) or (start_y == end_y)
    except AssertionError:
        raise LineTypeError("Line segment is not vertical or horizontal")

    if start_x == end_x:
        vertical_line(canvas, start_x, start_y, end_y, colour)
    else:
        horizontal_line(canvas, start_y, start_x, end_x, colour)
