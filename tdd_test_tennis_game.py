import unittest

from tdd_tennis_game import TennisGame


class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.tennis = TennisGame('player1', 'Apple')

    def test_love_all(self):
        self.given_player1_point(0)
        self.given_player2_point(0)
        self.score_result('Love - All')

    def test_fifteen_all(self):
        self.given_player1_point(1)
        self.given_player2_point(1)
        self.score_result('Fifteen - All')

    def test_thirty_all(self):
        self.given_player1_point(2)
        self.given_player2_point(2)
        self.score_result('Thirty - All')

    def test_deuce(self):
        self.given_player1_point(3)
        self.given_player2_point(3)
        self.score_result('Deuce')

    def test_player1_advantage(self):
        self.given_player1_point(5)
        self.given_player2_point(4)
        self.score_result('player1 Advantage')

    def test_player2_advantage(self):
        self.given_player1_point(4)
        self.given_player2_point(5)
        self.score_result('Apple Advantage')

    def test_player1_win(self):
        self.given_player1_point(7)
        self.given_player2_point(5)
        self.score_result('player1 Win')

    def test_love_fifteen(self):
        self.given_player1_point(0)
        self.given_player2_point(1)
        self.score_result('Love - Fifteen')

    def test_thirty_fifteen(self):
        self.given_player1_point(2)
        self.given_player2_point(1)
        self.score_result('Thirty - Fifteen')

    def test_forty_love(self):
        self.given_player1_point(3)
        self.given_player2_point(0)
        self.score_result('Forty - Love')

    def given_player1_point(self, time):
        for i in range(time):
            self.tennis.player1_win()

    def given_player2_point(self, time):
        for i in range(time):
            self.tennis.player2_win()

    def score_result(self, result):
        self.assertEqual(self.tennis.score(), result)


if __name__ == '__main__':
    unittest.main()
