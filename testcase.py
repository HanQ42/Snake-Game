import unittest

class BuggyTriangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3

    def right_triangle(self):
        return round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)


class BuggyTriangleTest(unittest.TestCase):
    def test_init(self):
        t = BuggyTriangle(3, 4, 5)
        self.assertEqual(t.a, 3)
        self.assertEqual(t.b, 4)
        self.assertEqual(t.c, 5)

    def test_right_triangle(self):
        t = BuggyTriangle(3, 4, 5)
        self.assertTrue(t.right_triangle())
        self.assertTrue(BuggyTriangle(5, 4, 3).right_triangle())
        self.assertFalse(BuggyTriangle(3, 3, 3).right_triangle())


if __name__ == '__main__':
    unittest.main(exit=False,verbosity=2)