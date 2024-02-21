import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('placeholder'.upper(), 'PLACEHOLDER')


if __name__ == '__main__':
    unittest.main()
