import random
import time

from mini_engine.player import IPlayer


class RandomBot(IPlayer):

    def next_move(self, board):
        print("Bot thinking")
        time.sleep(1)

        moved = False
        rnd = random.randint(0, board.remaining_counts() - 1)

        ctr = 0

        for x in range(3):
            for y in range(3):
                if (x, y) not in board.table:
                    if ctr == rnd:
                        board.add_token(x, y, self.token)
                        return

                    else:
                        ctr += 1
