from defaults import *


def canvas(width, height):
    """
    Creates a rectangular canvas using list of lists of strings

    :param width: width of canvas
    :param height: heiht of canvas
    :return: list of lists to store all positions of the canvas

    :Example:

    canvas(5,5) = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
    """
    c = []
    for x in range(height):
        c.append([DEFAULT_EMPTY] * width)
    return c


def height(canv):
    """
    gets the width of the canvas

    :param canv:
    :return: integer width of canvas
    """
    return len(canv)


def width(canv):
    """
    gets the height of the canvas

    :param canv:
    :return: integer height of the canvas
    """
    return (canv and len(canv[0])) or 0


def translate_1_based_to_0_based(x, y):
    """
    Translates 1 based co-ordinates to 0-based list indices

    :param x: x co-ordinate
    :param y: y co-ordinate
    :return: tuple of list indices corresponding to co-ordinates
    """
    return x-1, y-1


def set_colour(canv, x, y, colour=DEFAULT_COLOUR):
    """
    Sets colour at canvas co-ordinates x, y

    :param canv: canvas to manipulate
    :param x: x co-ordinate
    :param y: y co-ordinate
    :param colour: colour string (will be truncated to first character)
    :return: None
    """
    if is_point_in_canvas(canv, x, y):
        x, y = translate_1_based_to_0_based(x, y)
        canv[y][x] = colour[0]


def get_colour(canv, x, y):
    """
    Gets colour at canvas co-ordinates x, y

    :param canv: canvas to lookup
    :param x: x co-ordinate
    :param y: y co-ordinate
    :return: colour string (will be truncated to first character)
    """
    if is_point_in_canvas(canv, x, y):
        x, y = translate_1_based_to_0_based(x, y)
        return canv[y][x][0]


def is_x_in_canvas(canv, x):
    """
    Verifies if row x falls within canvas boundaries

    :param canv: canvas to bound by
    :param x: row x
    :return: boolean denoting whether row x is within canvas
    """
    return 1 <= x <= width(canv)


def is_y_in_canvas(canv, y):
    """
    Verifies if column y falls within canvas boundaries

    :param canv: canvas to bound by
    :param y: column y
    :return: boolean denoting whether column y is within canvas
    """
    return 1 <= y <= height(canv)


def is_point_in_canvas(canv, x, y):
    """
    Verifies if co-ordinates x, y fall within canvas boundaries

    :param canv:
    :param x: x co-ordinate
    :param y: y co-ordinate
    :return: boolean denoting whether position is within canvas
    """
    return is_x_in_canvas(canv, x) and is_y_in_canvas(canv, y)


def contain_x_range_to_canvas(canv, low_x, high_x):
    """
    Minimizes lower and upper bounds of a range of rows, to fall within canvas boundaries

    :param canv: canvas to bound by
    :param low_x: lower bound of range of rows
    :param high_x: upper bound of range of rows
    :return: minimised lazy sequence of rows
    """
    return xrange(max(1, low_x), min(high_x, width(canv))+1)


def contain_y_range_to_canvas(canv, low_y, high_y):
    """
    Minimizes lower and upper bounds of a range of columns, to fall within canvas boundaries

    :param canv: canvas to bound by
    :param low_y: lower bound of range of columns
    :param high_y: upper bound of range of columns
    :return: minimised lazy sequence of columns
    """
    return xrange(max(1, low_y), min(high_y, height(canv))+1)


def neighbour_coordinates(canv, x, y):
    """
    Gets the sequence of co-ordinates which are neighbours of the given co-ordinates

    :param canv: canvas in which to search for neighbours
    :param x: x co-ordinate
    :param y: y co-ordinate
    :return: sequence of co-ordinates
    """
    for neighbour_x in contain_x_range_to_canvas(canv, x-1, x+1):
        for neighbour_y in contain_y_range_to_canvas(canv, y-1, y+1):
            # skip input co-ordinates
            if neighbour_x != x or neighbour_y != y:
                yield neighbour_x, neighbour_y
