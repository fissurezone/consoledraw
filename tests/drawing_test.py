from drawing import *
import unittest


class TestDrawing(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.C = DEFAULT_COLOUR
        cls.E = DEFAULT_EMPTY

    @classmethod
    def teardown_class(cls):
        del cls.C

    def setUp(self):
        self.canvas_5_5 = canvas(5, 5)

    def tearDown(self):
        del self.canvas_5_5

    def assert_helper(self, actual, expected):
        """
        switches argument order from intuitive one to nose's canonical form
        """
        self.assertEqual(expected, actual)

    def assert_helper_pretty(self, actual, expected):
        """
        builds from expected pattern into canonical form:
         - list of lists of colours
         - with correct empty and default string colour
         and applies assertEquals against actual
        """
        expected = [list(x.strip("|"). replace(" ", self.E).replace("x", self.C)) for x in expected]
        self.assertEqual(expected, actual)

    def test_canvas_1_1(self):
        self.assert_helper(canvas(1, 1), [[self.E]])

    def test_canvas_5_5(self):
        self.assert_helper(canvas(5, 5), [[self.E] * 5] * 5)

    def test_point_top_left(self):
        point(self.canvas_5_5, 1, 1)
        expected = ["|x    |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_point_top_right(self):
        point(self.canvas_5_5, 5, 1)
        expected = ["|    x|",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_point_bottom_left(self):
        point(self.canvas_5_5, 1, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|x    |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_point_bottom_right(self):
        point(self.canvas_5_5, 5, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|    x|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_point_center(self):
        point(self.canvas_5_5, 3, 3)
        expected = ["|     |",
                    "|     |",
                    "|  x  |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_point_external(self):
        point(self.canvas_5_5, 6, 1)
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_not_vertical_and_not_horizontal_line(self):
        with self.assertRaises(LineTypeError):
            line(self.canvas_5_5, 1, 1, 2, 2)

    def test_line_upper_border(self):
        line(self.canvas_5_5, 1, 1, 5, 1)
        expected = ["|xxxxx|",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_lower_border(self):
        line(self.canvas_5_5, 1, 5, 5, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|xxxxx|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_left_border(self):
        line(self.canvas_5_5, 1, 1, 1, 5)
        expected = ["|x    |",
                    "|x    |",
                    "|x    |",
                    "|x    |",
                    "|x    |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_right_border(self):
        line(self.canvas_5_5, 5, 1, 5, 5)
        expected = ["|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_horizontal_row_3(self):
        line(self.canvas_5_5, 2, 3, 4, 3)
        expected = ["|     |",
                    "|     |",
                    "| xxx |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_vertical_col_3(self):
        line(self.canvas_5_5, 3, 2, 3, 4)
        expected = ["|     |",
                    "|  x  |",
                    "|  x  |",
                    "|  x  |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_horizontal_external(self):
        line(self.canvas_5_5, 6, 2, 6, 4)
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_line_vertical_external(self):
        line(self.canvas_5_5, 2, 6, 4, 6)
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_line_horizontal_partial_external_right(self):
        line(self.canvas_5_5, 2, 5, 6, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "| xxxx|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_horizontal_partial_external_left(self):
        line(self.canvas_5_5, 0, 5, 4, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|xxxx |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_horizontal_partial_external_left_right(self):
        line(self.canvas_5_5, 0, 5, 6, 5)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|     |",
                    "|xxxxx|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_vertical_partial_external_top(self):
        line(self.canvas_5_5, 5, 0, 5, 4)
        expected = ["|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_vertical_partial_external_bottom(self):
        line(self.canvas_5_5, 5, 2, 5, 6)
        expected = ["|     |",
                    "|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_line_vertical_partial_external_top_bottom(self):
        line(self.canvas_5_5, 5, 0, 5, 6)
        expected = ["|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|",
                    "|    x|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_not_ordered_coordinates_rectangle(self):
        with self.assertRaises(RectangleTypeError):
            rectangle(self.canvas_5_5, 2, 2, 1, 1)

    def test_rectangle_canvas_border(self):
        rectangle(self.canvas_5_5, 1, 1, 5, 5)
        expected = ["|xxxxx|",
                    "|x   x|",
                    "|x   x|",
                    "|x   x|",
                    "|xxxxx|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_internal(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 4)
        expected = ["|     |",
                    "| xxx |",
                    "| x x |",
                    "| xxx |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_fill_internal(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 4, self.C, True, "y")
        expected = ["|     |",
                    "| xxx |",
                    "| xyx |",
                    "| xxx |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_external(self):
        rectangle(self.canvas_5_5, 6, 1, 7, 2)
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_rectangle_external_surrounding(self):
        rectangle(self.canvas_5_5, 0, 0, 6, 6)
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_rectangle_fill_external(self):
        rectangle(self.canvas_5_5, 6, 1, 7, 2, self.C, True, "y")
        self.assert_helper(self.canvas_5_5, [[self.E] * 5] * 5)

    def test_rectangle_fill_external_surrounding(self):
        rectangle(self.canvas_5_5, 0, 0, 6, 6, self.C, True, "y")
        self.assert_helper(self.canvas_5_5, [["y"] * 5] * 5)

    def test_rectangle_partial_external_top_left(self):
        rectangle(self.canvas_5_5, 0, 0, 4, 2)
        expected = ["|   x |",
                    "|xxxx |",
                    "|     |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_partial_external_top_right(self):
        rectangle(self.canvas_5_5, 2, 0, 6, 2)
        expected = ["| x   |",
                    "| xxxx|",
                    "|     |",
                    "|     |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_partial_external_bottom_right(self):
        rectangle(self.canvas_5_5, 3, 4, 6, 6)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|  xxx|",
                    "|  x  |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_rectangle_partial_external_bottom_left(self):
        rectangle(self.canvas_5_5, 0, 4, 3, 6)
        expected = ["|     |",
                    "|     |",
                    "|     |",
                    "|xxx  |",
                    "|  x  |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_1_1(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 4)
        bucket_fill(self.canvas_5_5, 3, 3, ".")
        expected = ["|     |",
                    "| xxx |",
                    "| x.x |",
                    "| xxx |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_1_2(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 5)
        bucket_fill(self.canvas_5_5, 3, 3, ".")
        expected = ["|     |",
                    "| xxx |",
                    "| x.x |",
                    "| x.x |",
                    "| xxx |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_1_2_other_point(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 5)
        bucket_fill(self.canvas_5_5, 3, 4, ".")
        expected = ["|     |",
                    "| xxx |",
                    "| x.x |",
                    "| x.x |",
                    "| xxx |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_2_1(self):
        rectangle(self.canvas_5_5, 2, 2, 5, 4)
        bucket_fill(self.canvas_5_5, 3, 3, ".")
        expected = ["|     |",
                    "| xxxx|",
                    "| x..x|",
                    "| xxxx|",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_2_1_other_point(self):
        rectangle(self.canvas_5_5, 2, 2, 5, 4)
        bucket_fill(self.canvas_5_5, 4, 3, ".")
        expected = ["|     |",
                    "| xxxx|",
                    "| x..x|",
                    "| xxxx|",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_rectangle_fill_size_3_3(self):
        rectangle(self.canvas_5_5, 1, 1, 5, 5)
        bucket_fill(self.canvas_5_5, 3, 3, ".")
        expected = ["|xxxxx|",
                    "|x...x|",
                    "|x...x|",
                    "|x...x|",
                    "|xxxxx|"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_fill_rectangle_border(self):
        rectangle(self.canvas_5_5, 2, 2, 4, 4)
        bucket_fill(self.canvas_5_5, 4, 4, "!")
        expected = ["|     |",
                    "| !!! |",
                    "| ! ! |",
                    "| !!! |",
                    "|     |"]
        self.assert_helper_pretty(self.canvas_5_5, expected)

    def test_bucket_fill_complex(self):
        c = canvas(20, 4)
        line(c, 1, 2, 6, 2)
        expected = ["|                    |",
                    "|xxxxxx              |",
                    "|                    |",
                    "|                    |"]
        self.assert_helper_pretty(c, expected)

        line(c, 6, 3, 6, 4)
        expected = ["|                    |",
                    "|xxxxxx              |",
                    "|     x              |",
                    "|     x              |"]
        self.assert_helper_pretty(c, expected)

        rectangle(c, 14, 1, 18, 3)
        expected = ["|             xxxxx  |",
                    "|xxxxxx       x   x  |",
                    "|     x       xxxxx  |",
                    "|     x              |"]
        self.assert_helper_pretty(c, expected)

        bucket_fill(c, 10, 3, "o")
        expected = ["|oooooooooooooxxxxxoo|",
                    "|xxxxxxooooooox   xoo|",
                    "|     xoooooooxxxxxoo|",
                    "|     xoooooooooooooo|"]
        self.assert_helper_pretty(c, expected)
