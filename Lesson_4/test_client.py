import unittest
from Lesson_3.task.client import make_presence_msg


class test_make_presence_msg(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal(self):
        msg = make_presence_msg()
        self.assertEqual(msg['action'], "presence")


if __name__ == '__main__':
    unittest.main()
