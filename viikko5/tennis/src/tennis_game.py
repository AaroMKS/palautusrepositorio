class TennisGame:
    SCORE_LOVE = 0
    SCORE_FIFTEEN = 1
    SCORE_THIRTY = 2
    SCORE_FORTY = 3
    POINT_LIMIT = 4
    ADVANTAGE_DIFF = 1
    WIN_DIFF = 2

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = self.SCORE_LOVE
        self.m_score2 = self.SCORE_LOVE

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def _equal_score(self, score_names):
        if self.m_score1 < self.SCORE_FORTY:
            return f"{score_names[self.m_score1]}-All"
        else:
            return "Deuce"

    def _endgame_score(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == self.ADVANTAGE_DIFF:
            return f"Advantage {self.player1_name}"
        elif minus_result == -self.ADVANTAGE_DIFF:
            return f"Advantage {self.player2_name}"
        elif minus_result >= self.WIN_DIFF:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _regular_score(self, score_names):
        score1_text = score_names[self.m_score1]
        score2_text = score_names[self.m_score2]
        return f"{score1_text}-{score2_text}"

    def get_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.m_score1 == self.m_score2:
            return self._equal_score(score_names)

        elif self.m_score1 >= self.POINT_LIMIT or self.m_score2 >= self.POINT_LIMIT:
            return self._endgame_score()

        else:
            return self._regular_score(score_names)
