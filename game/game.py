import time

from game.board import Board
from mini_engine.game import IGame


class TicTacToeGame(IGame):
    def __init__(self, players: list, monitor: bool = True, fast_mode: bool = True, debug: bool = False):
        assert len(players) == 2
        self.monitor = monitor

        self.players = [
            players[0](token=1, fast_mode=fast_mode, debug=debug),
            players[1](token=2, fast_mode=fast_mode, debug=debug),
        ]
        self.board = Board()

        self.winner = None
        self.turn = 0

    def start(self):
        if self.monitor:
            print("Tic Tac Toa %s vs %s" % tuple(player.__class__.__name__ for player in self.players))
            self.board.print()

    def update(self):
        player = self.players[self.turn]

        if self.monitor:
            print(f"\nTurn {self.board.TOKEN_VERBOSE[player.token]}:")

        pos = player.get_move(self.board)
        self.board.add_token(pos, player.token)

        if self.monitor:
            self.board.print()

        # Check win conditions
        if self.board.is_winner(player.token):
            self.winner = player

            if self.monitor:
                self.board.print()
                print("Player %s won the game" % player)

            return False

        game_finished = self.board.is_full()
        self.turn = 1 - self.turn

        if game_finished and self.monitor:
            print("Game finished without winner!")

        return not game_finished
