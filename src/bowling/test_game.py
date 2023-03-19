import unittest
from bowling.frame import Frame
from bowling.game import BowlingGame

class TestGames(unittest.TestCase):

    def test_game(self):
        game = BowlingGame()
        frames_golden = []
        for i in range(0, 10):
            frame = Frame(i, 10-i)
            frames_golden.append(frame)
            game.add_frame(frame)
        frames = game.frames
        self.assertListEqual(frames, frames_golden)
        self.assertRaises(Exception, game.add_frame, Frame(0,0))

    def test_score(self):
        game = BowlingGame()
        for i in range(0, 10):
            frame = Frame(i, 9-i)
            game.add_frame(frame)
        score = game.score()
        self.assertEqual(score, 90)

    def test_score_strike(self):
        game = BowlingGame()
        first_frame = Frame(10,0)
        game.add_frame(first_frame)
        game.add_frame(Frame(3, 6))
        self.assertEqual(first_frame.score(), 19)
        self.assertEqual(game.score(), 28)

    def test_score_spare(self):
        game = BowlingGame()
        first_frame = Frame(1, 9)
        game.add_frame(first_frame)
        game.add_frame(Frame(3, 6))
        self.assertEqual(first_frame.score(), 13)  
        self.assertEqual(game.score(), 22)     

    def test_strike_and_spare(self):
        game = BowlingGame()
        strike_frame = Frame(10, 0)
        game.add_frame(strike_frame)
        spare_frame = Frame(4, 6)
        game.add_frame(spare_frame)
        game.add_frame(Frame(7, 2))
        self.assertEqual(strike_frame.score(), 20)
        self.assertEqual(spare_frame.score(), 17)
        self.assertEqual(game.score(), 46)

    def test_multiple_strikes(self):
        game = BowlingGame()
        strike_frame = Frame(10, 0)
        game.add_frame(strike_frame)
        strike2_frame = Frame(10, 0)
        game.add_frame(strike2_frame)
        game.add_frame(Frame(7, 2))
        self.assertEqual(strike_frame.score(), 27)
        self.assertEqual(strike2_frame.score(), 19)
        self.assertEqual(game.score(), 55)

    def test_multiple_spares(self):
        game = BowlingGame()
        for i in range(0, 9):
            frame = Frame(i, 10-i)
            game.add_frame(frame)
        game.add_frame(Frame(9,0))
        score = game.score()
        self.assertEqual(score, 144)

    def test_spare_as_last_frame(self):
        game = BowlingGame()
        for i in range(0, 9):
            game.add_frame(Frame(1,0))
        frame = Frame(9,1)
        game.add_frame(frame)
        self.assertEqual(frame.is_last_frame(), True)
        self.assertEqual(game.is_next_frame_bonus(), True)
        game.set_bonus(2, 0)
        self.assertEqual(frame.score(), 12)
        self.assertEqual(game.score(), 21)

    def test_strike_as_last_frame(self):
        game = BowlingGame()
        for i in range(0, 9):
            game.add_frame(Frame(1,0))
        frame = Frame(10,0)
        game.add_frame(frame)
        self.assertEqual(frame.is_last_frame(), True)
        self.assertEqual(game.is_next_frame_bonus(), True)
        game.set_bonus(2, 3)
        self.assertEqual(frame.score(), 15)
        self.assertEqual(game.score(), 24)  

    def test_bonus_is_strike(self):
        game = BowlingGame()
        for i in range(0, 9):
            game.add_frame(Frame(1,0))
        frame = Frame(9,1)
        game.add_frame(frame)
        self.assertEqual(frame.is_last_frame(), True)
        self.assertEqual(game.is_next_frame_bonus(), True)
        game.set_bonus(10, 0)
        self.assertEqual(frame.score(), 20)
        self.assertEqual(game.score(), 29)

    def test_best_score(self):
        game = BowlingGame()
        for i in range(0, 10):
            game.add_frame(Frame(10,0))
        self.assertEqual(game.is_next_frame_bonus(), True)
        game.set_bonus(10, 10)
        self.assertEqual(game.score(), 300)  

    def test_real_game(self):
        game = BowlingGame()
        game.add_frame(Frame(6,3))
        game.add_frame(Frame(7,1))
        game.add_frame(Frame(8,2))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(10,0))
        game.add_frame(Frame(6,2))
        game.add_frame(Frame(7,3))
        game.add_frame(Frame(10,0))
        game.add_frame(Frame(8,0))
        game.add_frame(Frame(7,3))
        game.set_bonus(10, 0)
        self.assertEqual(game.score(), 135)  

if __name__ == '__main__':
    unittest.main()
