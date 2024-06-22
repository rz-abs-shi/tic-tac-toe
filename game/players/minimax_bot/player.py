import random
import time

from game.board import Board
from game.players.minimax_bot.minimax import Minimax
from mini_engine.player import IPlayer


class MinimaxBot(IPlayer):

    def __init__(self, *args, **kwargs):
        super(MinimaxBot, self).__init__(*args, **kwargs)
        self.minimax = Minimax(Board(), self.token)

    def get_move(self, board):
        if not self.fast_mode:
            print("Bot is thinking")
            time.sleep(2)

        node = self.minimax.tree

        for m in board._moves:
            node = node.children.get(m)
            if not node:
                break
        else:
            child = self.minimax.get_max_child(node)
            if child:
                return child.key

        # Random select!
        free_pos = board.get_free_positions()
        if self.debug:
            print(f"Random move free_pos: {free_pos}")

        return random.choice(free_pos)
