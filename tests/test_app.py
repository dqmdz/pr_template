import unittest

from app.main import suma, resta, multi


class TestApp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1, 3), 4)

    def test_resta(self):
        self.assertEqual(resta(3, 1), 2)

    def test_multi(self):
        self.assertEqual(multi(2, 3), 8)


if __name__ == '__main__':
    unittest.main()
