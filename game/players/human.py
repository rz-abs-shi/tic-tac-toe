from mini_engine.player import IPlayer
from mini_engine.exceptions import ExitGameInterrupt


class Human(IPlayer):
    is_bot = False
    name = 'human'

    def get_move(self, board):
        while True:
            inp = input("Please Enter x y: ")
            if inp == 'exit':
                raise ExitGameInterrupt

            inp = inp.strip().split(' ')
            if len(inp) != 2:
                print("Invalid input. Try again.")
                continue

            try:
                x = int(inp[0].strip())
                y = int(inp[1].strip())
            except ValueError:
                continue

            position = x * 3 + y

            if board.is_empty(position):
                return position

            print("Invalid input. Try again.")
