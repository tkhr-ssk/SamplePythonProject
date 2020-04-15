import unittest
import main

from unittest.mock import patch


class TestMain(unittest.TestCase):

    def test_add_func(self):
        a = 1
        b = 2
        expected = 3
        actual = main.add_func(a, b)
        self.assertEqual(expected, actual)

    @patch('main.liba_sum')
    def test_lib_add_func(self, mock_sum):
        mock_sum.return_value = 3
        a = 100
        b = 200
        expected = 3
        actual = main.call_lib_add_func(a, b)
        self.assertEqual(expected, actual)

        a = 100
        b = 100
        expected = 3
        actual = main.call_lib_add_func(a, b)
        self.assertEqual(expected, actual)

    def test_main(self):
        main.main()


if __name__ == "__main__":
    unittest.main()
