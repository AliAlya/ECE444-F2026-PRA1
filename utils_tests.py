import unittest

from utilities import utils


class UtilsTests(unittest.TestCase):
    def test_reversed_with_integers(self):
        self.assertEqual(utils.reversed(9876), 6789)
        self.assertEqual(utils.reversed(4500), 54)
        self.assertEqual(utils.reversed(-246), -642)

    def test_reversed_with_string(self):
        with self.assertRaises(TypeError):
            utils.reversed("tried and failed")

    def test_reversed_with_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(82.64)

    def test_formatter_with_integer(self):
        self.assertEqual(utils.formatter(42), ("0b101010", "0o52"))

    def test_formatter_with_string(self):
        with self.assertRaises(TypeError):
            utils.formatter("tried and failed")

    def test_formatter_with_float(self):
        with self.assertRaises(TypeError):
            utils.formatter(31.75)


if __name__ == "__main__":
    unittest.main()
