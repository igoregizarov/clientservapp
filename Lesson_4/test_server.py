import unittest
from Lesson_3.task.server import send_msg_to_client


class test_make_presence_msg(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal(self):
        msg = send_msg_to_client('presence')
        self.assertEqual(msg['response'], 200)

    def test_equal(self):
        msg = send_msg_to_client('not_presence')
        self.assertEqual(msg['response'], 400)


if __name__ == '__main__':
    unittest.main()
