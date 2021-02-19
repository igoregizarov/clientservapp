import unittest


# assert 1 == 1, 'true'

def sum_sq(i, j):
    return i * i + j * j


class test_sum_sq(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal(self):
        self.assertEqual(sum_sq(2, 3), 13)


if __name__ == '__main__':
    unittest.main()
