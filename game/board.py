
class Board:
    BOARD_SIZE = 9

    def __init__(self):
        self.table = {}
        self.counter = 0

    def add_token(self, x, y, token):

        if 0 <= x < 3 and 0 <= y < 3 and not (x, y) in self.table:
            self.table[x, y] = token
            self.counter += 1

            return True

        return False

    def delete_token(self, x, y):
        if (x, y) in self.table:
            del self.table[x, y]
            self.counter -= 1
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

    def __len__(self):
        return self.counter

    def remaining_counts(self):
        return self.BOARD_SIZE - len(self)
