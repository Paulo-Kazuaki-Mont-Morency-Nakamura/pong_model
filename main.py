# Here is the main code to run the "Game"

import sys
from pong_modules import pong_game

if __name__ == '__main__':
    game = pong_game.Game()

    # Adding other classes to the game class
    game.reset_game()

    game.run()