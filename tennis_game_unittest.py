import unittest

from tennis_game import TennisGame

test_cases = [
# 同分的情況
(0,0, 'Love - All', 'player1', 'player2'),
(1,1, 'Fifteen - All', 'player1', 'player2'),
(2,2, 'Thirty - All', 'player1', 'player2'),
(3,3, 'Deuce', 'player1', 'player2'),
(4,4, 'Deuce', 'player1', 'player2'),

# 固定一方為 Love
(0,1, 'Love - Fifteen', 'player1', 'player2'),
(1,0, 'Fifteen - Love', 'player1', 'player2'),
(0,2, 'Love - Thirty', 'player1', 'player2'),
(2,0, 'Thirty - Love', 'player1', 'player2'),
(0,3, 'Love - Forty', 'player1', 'player2'),
(3,0, 'Forty - Love', 'player1', 'player2'),
(0,4, 'player2 Win', 'player1', 'player2'),
(4,0, 'player1 Win', 'player1', 'player2'),

# 固定一方為 Fifteen
(2,1, 'Thirty - Fifteen', 'player1', 'player2'),
(1,2, 'Fifteen - Thirty', 'player1', 'player2'),
(3,1, 'Forty - Fifteen', 'player1', 'player2'),
(1,3, 'Fifteen - Forty', 'player1', 'player2'),
(4,1, 'player1 Win', 'player1', 'player2'),
(1,4, 'player2 Win', 'player1', 'player2'),

# 固定一方為 Thirty
(3,2, 'Forty - Thirty', 'player1', 'player2'),
(2,3, 'Thirty - Forty', 'player1', 'player2'),
(4,2 , 'player1 Win', 'player1', 'player2'),
(2,4, 'player2 Win', 'player1', 'player2'),

# Advantage 情境
(4,3, 'player1 Advantage', 'player1', 'player2'),
(3,4, 'player2 Advantage', 'player1', 'player2'),
(5,4, 'player1 Advantage', 'player1', 'player2'),
(4,5, 'player2 Advantage', 'player1', 'player2'),
(10,9, 'player1 Advantage', 'player1', 'player2'),
(9,10, 'player2 Advantage', 'player1', 'player2'),

# 勝利
(6,4, 'player1 Win', 'player1', 'player2'),
(4,6, 'player2 Win', 'player1', 'player2'),
(11,9, 'player1 Win', 'player1', 'player2'),
(9,11, 'player2 Win', 'player1', 'player2'),
]


def game_start(tennis_game, player1, player2, player1_point, player2_point):
	game = tennis_game(player1, player2)
	for i in range(max(player1_point, player2_point)):
		if i < player1_point:
			game.win_score(player1)

		if i < player2_point:
			game.win_score(player2)

	return game


class TestTennisGame(unittest.TestCase):
	def test_tennis_score(self):
		for test_case in test_cases:
			player1_point, player2_point, score, player1, player2 = test_case

			game = game_start(TennisGame, player1, player2, player1_point, player2_point)

			self.assertEqual(score, game.score())

if __name__ =='__main__':
	unittest.main()
		





