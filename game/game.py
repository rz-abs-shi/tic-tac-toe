from mini_engine.game import IGame
from game.board import Board
from game.players import Human, RandomBot, SmartBot
import time
import os


class TicTacToeGame(IGame):
    first_player = RandomBot
    second_player = SmartBot

    def start(self):
        self.board = Board()
        self.players = [self.first_player('X', 'O'), self.second_player('O', 'X')]
        self.turn = 0
        print ("Tic Tac Toa %s vs %s" % tuple(player.__class__.__name__ for player in self.players))

    def update(self):
        os.system('cls')
        self.board.print()

        player = self.players[self.turn]

        if player.is_bot:
            print("Bot is thinking")
            time.sleep(1)

        player.next_move(self.board)
        self.turn = 1 - self.turn

        # Check win conditions
        for token in ['X', 'O']:
            if self.board.does_token_won(token):
                self.board.print()

                print ("Player %s won the game" % token)
                return False

        return not self.board.is_full()
