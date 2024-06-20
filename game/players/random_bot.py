import random
import time

from mini_engine.player import IPlayer


class RandomBot(IPlayer):

    def get_move(self, board):
        if not self.fast_mode:
            print("Bot is thinking")
            time.sleep(2)

        free_pos = board.get_free_positions()
        if self.debug:
            print(f"free_pos: {free_pos}")

        return random.choice(free_pos)
