class Score:
    def __init__(self):
        self.points = 0
        self.attempts = 1

    def reward_hit(self, amount):
        self.points += amount

    def penalty(self):
        self.attempts += 1

    def reset(self):
        self.points = 0
        self.attempts = 1

    def draw(self):
        print(f'||[PLAYER] < Score: {self.points} | Attempts: {self.attempts} >')