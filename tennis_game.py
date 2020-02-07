class TennisGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1_point = 0
        self.player2_point = 0

    def win_score(self, player):
        if player == self.player1:
            self.player1_point += 1
        else:
            self.player2_point += 1

    def score(self):
        result = ''
        temp_point1 = 0
        temp_point2 = 0

        if self.player1_point == self.player2_point:
            # 同分狀態
            result = {
                0: 'Love - All',
                1: 'Fifteen - All',
                2: 'Thirty - All',
            }.get(self.player1_point, 'Deuce')
        elif (self.player1_point >= 4 or self.player2_point >= 4):
            # Deuce後續狀況
            diff_score = self.player1_point - self.player2_point

            if diff_score == 1:
                result = '{} Advantage'.format(self.player1)
            elif diff_score == -1:
                result = '{} Advantage'.format(self.player2)
            elif diff_score >= 2:
                result = '{} Win'.format(self.player1)
            else:
                result = '{} Win'.format(self.player2)

        else:
            for i in range(1, 3):
                if (i == 1):
                    temp_point1 = self.player1_point
                else:
                    temp_point2 = self.player2_point

                score_result = {
                    0: 'Love',
                    1: 'Fifteen',
                    2: 'Thirty',
                    3: 'Forty',
                }

                result = '{} - {}'.format(score_result[temp_point1], score_result[temp_point2])

        return result
