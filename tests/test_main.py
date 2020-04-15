import unittest

import main


class TestMain(unittest.TestCase):

    def test_add_func(self):
        a = 1
        b = 2
        expected = 3
        actual = main.add_func(a, b)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
