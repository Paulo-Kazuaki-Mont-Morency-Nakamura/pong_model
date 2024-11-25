BASE_X = 300
BASE_Y = 300

BASE_SPEED_X = 4
BASE_SPEED_Y = 4

class Ball:
    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height
        self.x = BASE_X
        self.y = BASE_Y
        self.speed_x = BASE_SPEED_X
        self.speed_y = BASE_SPEED_Y

        self.moving = False
        self.hit_text = None

        self.wall_tick = 0
        self.hits = 0

    def toggle_movement(self, toggle):
        self.moving = toggle

    def reset(self):
        self.x = BASE_X
        self.y = BASE_Y
        self.speed_x = BASE_SPEED_X
        self.speed_y = BASE_SPEED_Y
        self.moving = False

    def update(self):
        self.wall_tick += 1

        if self.moving:
            self.x += self.speed_x
            self.y += self.speed_y

        return self.x, self.y

    def border_collision(self, game, max_width, max_height):
        self.hit_text = None

        if self.wall_tick > 15:
            # Checking wall collision
            if self.x <= 0 or self.x + self.width >= max_width:
                self.wall_tick = 0
                self.speed_x *= -1

                self.hit_text = '- A bola bateu na parede!'

            # Checking top collision
            if self.y <= 0:
                self.wall_tick = 0
                self.speed_y *= -1

                self.hit_text = '- A bola bateu no teto!'

            # Checking floor collision
            if self.y + self.height >= max_height:
                self.wall_tick = 0
                self.speed_y *= -1

                game.score.penalty()

                self.hit_text = '- A bola bateu no chão!'

    def draw(self):
        print('\n||[BALL] X: {:03d} | Y: {:03d}'.format(self.x, self.y))
        if self.hit_text: print(self.hit_text)