class TennisGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1_point = 0
        self.player2_point = 0

    def player1_win(self):
        self.player1_point += 1

    def player2_win(self):
        self.player2_point += 1

    def score(self):
        result = ''

        if self.player1_point == self.player2_point:
            result = {
                0: 'Love - All',
                1: 'Fifteen - All',
                2: 'Thirty - All',
            }.get(self.player1_point, 'Deuce')

        elif (self.player1_point >= 4 or self.player2_point >= 4):
            diff_score = self.player1_point - self.player2_point

            if diff_score == 1:
                result = '{} Advantage'.format(self.player1)
            elif diff_score == -1:
                result = '{} Advantage'.format(self.player2)
            elif diff_score == 2:
                result = '{} Win'.format(self.player1)
            else:
                result = '{} Win'.format(self.player2)

        else:
            score_result = {
                0: 'Love',
                1: 'Fifteen',
                2: 'Thirty',
                3: 'Forty',
            }
            result = '{} - {}'.format(score_result[self.player1_point], score_result[self.player2_point])

        return result
