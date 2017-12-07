from defaults import *
from canvas import width, height, get_colour, neighbour_coordinates
from Queue import Queue
from point import point


def bucket_fill(canvas, point_x, point_y, colour):
    """
    sets colour to all co-ordinates, which are co-contained,
    along with point_x, point_y, by some shape, and bounded by canvas

    :param canvas: canvas to manipulate
    :param point_x: x co-ordinate
    :param point_y: y co-ordinate
    :param colour: colour to set at points
    :return: None

    :Example:

    c = canvas(5,5)
    rectangle(c, 2, 2, 6, 6)
    bucket_fill(c, 4, 4, "y") == [[' ', ' ', ' ', ' ', ' '],
                                  [' ', 'x', 'x', 'x', 'x'],
                                  [' ', 'x', 'y', 'y', 'y'],
                                  [' ', 'x', 'y', 'y', 'y'],
                                  [' ', 'x', 'y', 'y', 'y']]
    """
    search_colour = get_colour(canvas, point_x, point_y)

    def same_colour_neighbour_coordinates(x, y):
        # closure of canvas and search_colour
        for neigh_x, neigh_y in neighbour_coordinates(canvas, x, y):
            if get_colour(canvas, neigh_x, neigh_y) == search_colour:
                yield neigh_x, neigh_y

    # modified bfs all connected co-ordinates of same colour
    observed = set()
    unvisited = Queue(maxsize=width(canvas)*height(canvas))
    unvisited.put((point_x, point_y))
    while not unvisited.empty():
        x, y = unvisited.get()
        # fill co-ordinate with new colour
        point(canvas, x, y, colour)

        # find connected unvisited co-ordinates of original colour
        for neighbour_x, neighbour_y in same_colour_neighbour_coordinates(x, y):
            if (neighbour_x, neighbour_y) not in observed:
                unvisited.put((neighbour_x, neighbour_y))
                observed.add((neighbour_x, neighbour_y))
