import unittest

class TestMy(unittest.TestCase):
    def test_true(self):
        self.assertEqual('foo', 'foo')

    def test_false(self):
        self.assertNotEqual(True, False)

if __name__ == '__main__':
    unittest.main()