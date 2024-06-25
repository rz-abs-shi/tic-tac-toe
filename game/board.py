from copy import deepcopy


class Board:
    TOKEN_VERBOSE = ('-', 'X', 'O')
    TOKENS = (1, 2)

    WINS = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    def __init__(self):
        self._table = [0] * 9
        self._size = 0
        self._moves = []

    def set_moves(self, moves: list):
        for m in moves:
            self.add_token(m, self.get_turn())

    def undo(self):
        if not self._moves:
            return

        p = self._moves.pop()
        self._size -= 1
        self._table[p] = 0

    def clone(self):
        return deepcopy(self)

    def get_turn(self):
        return (self._size % 2) + 1

    def add_token(self, position: int, token: int):
        assert token in self.TOKENS
        assert 0 <= position < 9
        assert not self._table[position]

        self._table[position] = token
        self._size += 1
        self._moves.append(position)

    def is_full(self):
        return self._size == 9

    def is_winner(self, token: int):
        assert token in self.TOKENS
        for win in self.WINS:
            win_pos = list(filter(lambda pos: self._table[pos] == token, win))

            if len(win_pos) == len(win):
                return True

        return False

    def __str__(self):
        return self.get_str()

    def get_str(self, with_pos = False):
        rows = []

        moves_map = {self._moves[i]: i for i in range(len(self._moves))}

        for x in range(3):
            row = ""
            start = True

            for y in range(3):

                if not start:
                    row += "|"
                else:
                    start = False

                pos = x * 3 + y
                token = self._table[pos]
                row += self.TOKEN_VERBOSE[token]

                if with_pos and token > 0:
                    row += f':{moves_map[pos]}'

            rows.append(row)
        return '\n'.join(rows)

    def print(self):
        print(self)

    @property
    def cap(self):
        return 9

    @property
    def size(self):
        return self._size

    @property
    def remaining(self):
        return self.cap - self.size

    def get_free_positions(self):
        return list(filter(lambda pos: not self._table[pos], range(9)))

    def is_empty(self, pos: int):
        return self._table[pos] == 0
