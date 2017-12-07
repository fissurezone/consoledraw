import os
import sys
from drawing import *
from pyparsing import Word, nums, printables, ParseException

# Global canvas
canv = canvas(40, 10)


def draw():
    os.system("cls")
    print("-"*(width(canv)+2))
    for row in xrange(height(canv)):
        print("|" + "".join(canv[row]) + "|")
    print("-" * (width(canv) + 2))


def create_canvas(*args):
    global canv
    # delete current canvas and create new one
    del canv
    canv = canvas(*args)


def canvas_factory(shape):
    global canv

    # closure of lower order function 'shape'
    # which would be one of the shape drawing functions: line, rectangle, bucket_fill
    def closure(*args):
        shape(canv, *args)
    return closure


command_factory = {"Q": quit,
                   "C": create_canvas,
                   "L": canvas_factory(line),
                   "R": canvas_factory(rectangle),
                   "B": canvas_factory(bucket_fill)}


if __name__ == "__main__":
    num = Word(nums).setParseAction(lambda x: int(x[0]))
    dims = num + num
    coords = num + num
    colour = Word(printables, max=1)

    die = Word("Q", max=1)
    can = Word("C", max=1) + dims
    lin = Word("L", max=1) + coords + coords
    rec = Word("R", max=1) + coords + coords
    fil = Word("B", max=1) + coords + colour
    commands = die | can | lin | rec | fil

    draw()
    while True:
        try:
            tokens = commands.parseString(raw_input("enter command: "))
        except ParseException:
            sys.stderr.write("Could not parse command.\n"
                             "Help: Q - quit | C w h - new canvas | L x1 y1 x2 y2 - new line from x1,y1 to x2,y2 |\n"
                             "      R x1 y1 x2 y2 - new rectangle, with top left at x1,y1, bottom right at x2,y2 |\n"
                             "      B x y c - fill the entire area connected to x,y with \"colour\" c\n")
            continue

        func = command_factory[tokens[0]]
        args = tokens[1:]
        try:
            func(*args)
        except DrawingError, e:
            sys.stderr.write("Could not perform action because {}\n".format(str(e)))
            continue

        draw()
