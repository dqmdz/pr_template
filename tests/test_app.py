import unittest

from app.main import suma, resta


class TestApp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1, 3), 4)

    def test_resta(self):
        self.assertEqual(resta(3, 1), 4)


if __name__ == '__main__':
    unittest.main()
