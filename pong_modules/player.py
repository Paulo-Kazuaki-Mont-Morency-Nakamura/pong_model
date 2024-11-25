from pong_modules import paddle

class Player:
    def __init__(self, index):
        self.index = index
        self.points = 0
        self.paddle = paddle.Paddle(self.index)

    def reward(self, amount):
        self.points += amount

    def reset(self):
        self.points = 0

    def draw(self):
        print(f'||[PLAYER {self.index}] < Score: {self.points} >')
        self.paddle.draw()