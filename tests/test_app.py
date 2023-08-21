import unittest

from app.main import suma


class TestApp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1, 3), 4)


if __name__ == '__main__':
    unittest.main()
