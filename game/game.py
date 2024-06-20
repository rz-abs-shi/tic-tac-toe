import time

from game.board import Board
from mini_engine.game import IGame


class TicTacToeGame(IGame):
    def __init__(self, players: list, move_delay: int = 0):
        assert len(players) == 2
        assert move_delay >= 0

        self.first_player = players[0]
        self.second_player = players[1]

        self.move_delay = move_delay
        self.players = [players[0]('X'), players[1]('O')]
        self.board = Board()

        self.winner = None
        self.turn = 0

    def start(self):
        print("Tic Tac Toa %s vs %s" % tuple(player.__class__.__name__ for player in self.players))
        self.board.print()

    def update(self):
        player = self.players[self.turn]

        if player.is_bot:
            print("Bot is thinking")

            if self.move_delay:
                time.sleep(self.move_delay)

        player.next_move(self.board)
        self.board.print()

        # Check win conditions
        for token in ['X', 'O']:
            if self.board.is_winner(token):
                self.board.print()
                self.winner = player
                print("Player %s won the game" % token)
                return False

        game_finished = self.board.is_full()
        self.turn = 1 - self.turn

        return not game_finished
