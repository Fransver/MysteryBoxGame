class Score:
    def __init__(self):
        self.score = 0

    def update_score_win(self):
        self.score = 1

    def update_score_loss(self):
        self.score = 2
