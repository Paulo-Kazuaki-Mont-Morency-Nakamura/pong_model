class Paddle:
    def __init__(self, player_index):
        self.width = 20
        self.height = 60
        self.player_index = player_index

        if player_index == 1:
            base_x = 10
        else:
            base_x = 600

        self.base_x = base_x
        self.x = base_x
        self.y = 240

        self.speed = 10
        self.collide_text = None

    def reset(self):
        self.x = self.base_x
        self.y = 240

    def move(self, direction):
        self.collide_text = None

        if direction == 'up':
            if self.y - self.speed >= 0:
                self.y -= self.speed
            else:
                self.collide_text = f"O jogador {self.player_index} está no teto."
        elif direction == 'down':
            if self.y + self.width + self.speed <= 600:
                self.y += self.speed
            else:
                self.collide_text = f"O jogador {self.player_index} está no chão."


    def draw(self):
        print('||[PADDLE {:d}] X: {:03d} | Y: {:03d}\n'.format(self.player_index, self.x, self.y))
        if self.collide_text: print(self.collide_text)

