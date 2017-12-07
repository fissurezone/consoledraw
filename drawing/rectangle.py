from defaults import *
from line import line
from point import point
from canvas import contain_x_range_to_canvas, contain_y_range_to_canvas


def rectangle(canvas, top_left_x, top_left_y, bottom_right_x, bottom_right_y, border=DEFAULT_COLOUR,
              fill=False, fill_colour=DEFAULT_EMPTY):
    """
    Creates a rectangle given its top-left and bottom-right co-ordinates

    :param canvas: canvas to manipulate
    :param top_left_x: x co-ordinate of top-left
    :param top_left_y: y co-ordinate of top-left
    :param bottom_right_x: x co-ordinate of bottom-right
    :param bottom_right_y: y co-ordinate of bottom-right
    :param border: colour to set at
    :param fill: boolean flag indicating if the rectangle is to be filled
    :param fill_colour: colour to fill the inside of the rectangle
    :return: None
    :raises RectangleTypeError: when 'bottom-right' is not really below and to the right of 'top-left'

    :Example:

    rectangle(canvas(5,5), 2, 2, 4, 4) == [[' ', ' ', ' ', ' ', ' '],
                                           [' ', 'x', 'x', 'x', ' '],
                                           [' ', 'x', ' ', 'x', ' '],
                                           [' ', 'x', 'x', 'x', ' '],
                                           [' ', ' ', ' ', ' ', ' ']]
    """
    # function expects top left and bottom right co-ordinates
    try:
        assert top_left_x <= bottom_right_x and top_left_y <= bottom_right_y
    except AssertionError:
        raise RectangleTypeError("Co-ordinates top-left {},{} are not above "
                                 "and to the left of co-ordinates bottom-right {},{}"
                                 .format(top_left_x, top_left_y, bottom_right_x, bottom_right_y))

    # draw lines upper left - upper right, upper right - bottom right, bottom right - bottom left,
    # and finally, bottom left - upper left
    upper_left = (top_left_x, top_left_y)
    upper_right = (bottom_right_x, top_left_y)
    bottom_right = (bottom_right_x, bottom_right_y)
    bottom_left = (top_left_x, bottom_right_y)

    def rect_border_line(start_x, start_y, end_x, end_y):
        # closure of canvas and border
        line(canvas, start_x, start_y, end_x, end_y, border)

    rect_border_line(*(upper_left + upper_right))
    rect_border_line(*(upper_right + bottom_right))
    rect_border_line(*(bottom_right + bottom_left))
    rect_border_line(*(bottom_left + upper_left))

    if fill:
        # set points inside the rectangle borders
        for x in contain_x_range_to_canvas(canvas, top_left_x, bottom_right_x):
            for y in contain_y_range_to_canvas(canvas, top_left_y, bottom_right_y):
                # exclude borders
                if x not in (top_left_x, bottom_right_x) and y not in (top_left_y, bottom_right_y):
                    point(canvas, x, y, fill_colour)
