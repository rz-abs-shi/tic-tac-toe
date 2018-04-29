from mini_engine.player import IPlayer
from mini_engine.exceptions import ExitGameInterrupt


class Human(IPlayer):
    is_bot = False

    def next_move(self, board):
        input_got = False
        while not input_got:
            inp = input("Please Enter x,y: ")
            if inp == 'exit':
                raise ExitGameInterrupt

            inp = inp.split(',')
            if len(inp) != 2:
                continue

            try:
                x = int(inp[0])
                y = int(inp[1])
            except:
                continue

            if board.add_token(x, y, self.token):
                input_got = True

