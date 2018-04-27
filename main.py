import random
import time


class Board:
    def __init__(self):
        self.table = {}
        self.counter = 0

    def add_token(self, x, y, token):

        if 0 <= x < 3 and 0 <= y < 3 and not (x, y) in self.table:
            self.table[x, y] = token
            self.counter += 1

            return True

        return False

    def is_full(self):
        return self.counter == 9

    def get_token(self, x, y):
        if (x, y) in self.table:
            return self.table[x, y]

    def does_token_won(self, token):

        for x in range(3):

            won = True
            for y in range(3):
                if self.get_token(x, y) != token:
                    won = False
                    break
            if won:
                return True

        for y in range(3):
            won = True
            for x in range(3):
                if self.get_token(x, y) != token:
                    won = False
                    break
            if won:
                return True

        won = True
        for i in range(3):
            if self.get_token(i, i) != token:
                won = False
                break

        if won:
            return True

        won = True
        for i in range(3):
            if self.get_token(i, 2 - i) != token:
                won = False
                break

        if won:
            return True

        return False

    def print(self):

        for x in range(3):
            row = ""
            start = True

            for y in range(3):

                if not start:
                    row += "|"

                else:
                    start = False

                if (x, y) in self.table:
                    row += self.table[x, y]

                else:
                    row += '-'

            print(row)


class IGame:

    def run_loop(self):

        self.start()

        while self.update():
            pass

    def start(self):
        pass

    def update(self):
        pass


class IPlayer:

    def __init__(self, token):
        self.token = token

    def next_move(self, board):
        pass

class Human(IPlayer):

    def next_move(self, board):
        input_got = False
        while not input_got:
            try:
                inp = input("Please Enter x,y: ").split(',')

                if len(inp) != 2:
                    continue

                x = int(inp[0])
                y = int(inp[1])

                if board.add_token(x, y, self.token):
                    input_got = True
            except:
                continue

class Bot(IPlayer):

    def next_move(self, board):
        print("Bot thinking")
        time.sleep(1)

        moved = False

        for x in range(3):
            if moved:
                break
            for y in range(3):
                if (x, y) not in board.table:
                    board.add_token(x, y, self.token)
                    moved = True
                    break

        if not moved:
            raise Exception("Board is full")


class TicTacToeGame(IGame):

    def start(self):
        self.board = Board()
        self.players = [Human('X'), Bot('O')]
        self.turn = 0

    def update(self):

        self.board.print()
        print()

        self.players[self.turn].next_move(self.board)
        self.turn = 1 - self.turn

        # Check win conditions
        for token in ['X', 'O']:
            if self.board.does_token_won(token):
                self.board.print()

                print ("Player %s won the game" % token)
                return False

        return not self.board.is_full()


if __name__ == '__main__':
    game = TicTacToeGame()

    game.run_loop()
