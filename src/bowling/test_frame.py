import unittest

from bowling.frame import Frame


class TestFrames(unittest.TestCase):

    def test_throughs(self):
        frame = Frame(2, 4)
        self.assertEqual(frame.first_throw, 2)
        self.assertEqual(frame.second_throw, 4)

    def test_frame_values(self):
        self.assertRaises(Exception, Frame, 11, 1)
        self.assertRaises(Exception, Frame, 2, 20)
        self.assertRaises(Exception, Frame, 10, 10)

    def test_score(self):
        frame = Frame(2, 6)
        score = frame.score()
        self.assertEqual(score, 8)

    def test_strike(self):
        frame = Frame(10,0)
        self.assertEqual(frame.is_strike(), True)

    def test_spare(self):
        frame = Frame(1,9)
        self.assertEqual(frame.is_spare(), True)

if __name__ == '__main__':
    unittest.main()
