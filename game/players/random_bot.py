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
            if moved:
                break
            for y in range(3):
                if (x, y) not in board.table:
                    if ctr == rnd:
                        board.add_token(x, y, self.token)
                        moved = True
                        break

                    else:
                        ctr += 1

        if not moved:
            raise Exception("Board is full")

