from mini_engine.player import IPlayer
from mini_engine.exceptions import ExitGameInterrupt


class Human(IPlayer):
    is_bot = False

    def _next_move(self, board):
        while True:
            inp = input("Please Enter x,y: ")
            if inp == 'exit':
                raise ExitGameInterrupt

            inp = inp.split(',')
            if len(inp) != 2:
                continue

            try:
                x = int(inp[0].strip())
                y = int(inp[1].strip())
            except:
                continue

            if board.add_token(x, y, self.token):
                return

            print("Invalid input. Try again")
