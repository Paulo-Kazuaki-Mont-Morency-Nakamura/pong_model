class Paddle:
    def __init__(self):
        self.width = 3
        self.height = 60
        self.speed = 10
        self.x = 10
        self.y = 240

        self.shrink = False
        self.collide_text = None

    def reset(self):
        self.x = 10
        self.y = 240
        self.width = 3

    def shrink_paddle(self):
        self.width = 20

    def move(self, direction):
        self.collide_text = None

        if direction == 'up':
            if self.y - self.speed >= 0:
                self.y -= self.speed
            else:
                self.collide_text = "O jogador está no teto."
        elif direction == 'down':
            if self.y + self.width + self.speed <= 600:
                self.y += self.speed
            else:
                self.collide_text = "O jogador está no chão."


    def draw(self):
        print('\n||[PADDLE] X: {:03d} | Y: {:03d}'.format(self.x, self.y))
        if self.collide_text: print(self.collide_text)

