# Here is the main code to run the "Game"
import time
import keyboard

from pong_modules import ball
from pong_modules import player

# "Game" is a class, and serves access to all variables inside it along with the main loop
class Game:
    def __init__(self):
        # Screen sizes
        self.screen_width = 640
        self.screen_height = 480
        self.FPS = 60
        self.tick = 0

        # Game loop
        self.running = True
        self.on_menu = True

        # Classes (they are added in "main")
        self.ball = ball.Ball()
        self.player_1 = player.Player(1)
        self.player_2 = player.Player(2)

        # Text information to print
        self.clear_space_text = 8 * '\n'

    def reset_game(self):
        # Clearing for menu
        print(self.clear_space_text)
        print('---------- MENU ----------')
        self.player_1.draw()
        self.player_2.draw()

        print('\n- Aperte ENTER para iniciar')

        self.player_1.reset()
        self.player_2.reset()
        self.ball.reset()
        self.on_menu = True

    def run(self):
        # Starting ball movement
        frame_duration = 1 / self.FPS

        while self.running:
            self.tick += 1

            # making sure the game runs at 60 frames per second
            start_time = time.time()
            elapsed_time = time.time() - start_time

            if elapsed_time < frame_duration:
                time.sleep(frame_duration - elapsed_time)

            self.handle_events()

            if not self.on_menu:
                self.update_game()

            self.draw()


    def handle_events(self):
        # Player paddle movement
        if self.on_menu:
            if keyboard.is_pressed('enter'):
                self.on_menu = False
                self.ball.toggle_movement(True)

        else:
            if keyboard.is_pressed('w'):
                 self.player_1.move('up')
            if keyboard.is_pressed('s'):
                 self.player_1.move('down')

            if keyboard.is_pressed('up'):
                 self.player_2.move('up')
            if keyboard.is_pressed('down'):
                 self.player_2.move('down')


        if keyboard.is_pressed('esc'):
            print("Encerrando o programa.")
            self.running = False

    def update_game(self):
        # Finishing game if needed
        p1_score = self.player_1.points
        p2_score = self.player_2.points
        if p1_score >= 2 or p2_score >= 2: self.reset_game()

        # Updating the ball and checking collisions
        self.ball.toggle_movement(True)
        self.ball.update()
        self.ball.border_collision(self, self.screen_width, self.screen_height)
        self.ball.paddle_collision(self.player_1)
        self.ball.paddle_collision(self.player_2)


    def draw(self):
        # Slowly updating screen
        if self.tick % 15 == 0:
            if not self.on_menu:
                print(self.clear_space_text)

                print('----- Pong MODEL -----')
                self.player_1.draw()
                self.player_2.draw()
                self.ball.draw()