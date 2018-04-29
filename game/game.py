from mini_engine.game import IGame
from game.board import Board
from game.players import Human, RandomBot


class TicTacToeGame(IGame):

    def start(self):
        self.board = Board()
        self.players = [Human('X'), RandomBot('O')]
        self.turn = 0
        print ("Tic Tac Toa %s vs %s" % (Human.__name__, RandomBot.__name__))

    def update(self):

        self.board.print()

        self.players[self.turn].next_move(self.board)
        self.turn = 1 - self.turn

        # Check win conditions
        for token in ['X', 'O']:
            if self.board.does_token_won(token):
                self.board.print()

                print ("Player %s won the game" % token)
                return False

        return not self.board.is_full()
