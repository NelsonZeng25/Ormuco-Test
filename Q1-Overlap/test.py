import unittest
from line_overlap import *

class TestOverlap(unittest.TestCase):

    def test_both_positive(self):
        line1 = Line(1, 5)
        line2 = Line(2, 6)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(0, 5)
        line2 = Line(5, 10)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(1, 5)
        line2 = Line(6, 8)
        self.assertEqual(overlap(line1, line2), False)

        line1 = Line(5, 10)
        line2 = Line(5, 10)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(5, 10)
        line2 = Line(1, 2)
        self.assertEqual(overlap(line1, line2), False)
    
    def test_negative_input(self):
        line1 = Line(-5, -2)
        line2 = Line(-4, 0)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(-10, -8)
        line2 = Line(-25, -15)
        self.assertEqual(overlap(line1, line2), False)

        line1 = Line(-6, 5)
        line2 = Line(2, 7)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(-10, 10)
        line2 = Line(-20, -2)
        self.assertEqual(overlap(line1, line2), True)

    def test_switch_input_order(self):
        line1 = Line(5, 0)
        line2 = Line(3, 10)
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line(10, 5)
        line2 = Line(4, 1)
        self.assertEqual(overlap(line1, line2), False)

        line1 = Line(10, -4)
        line2 = Line(-7, -12)
        self.assertEqual(overlap(line1, line2), False)

    def test_string_input(self):
        line1 = Line("hello", 6)
        line2 = Line(1, "good day")
        self.assertEqual(overlap(line1, line2), False)

        line1 = Line("10", 5)
        line2 = Line(5, "10")
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line("0", 5)
        line2 = Line("", 10)
        self.assertEqual(overlap(line1, line2), False)

        line1 = Line("1", "10")
        line2 = Line("5", "10")
        self.assertEqual(overlap(line1, line2), True)

        line1 = Line("@@", "12##")
        line2 = Line(5, 10)
        self.assertEqual(overlap(line1, line2), False)


if __name__ == '__main__':
    unittest.main()