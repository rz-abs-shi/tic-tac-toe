
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

    def print(self):
        for x in range(3):
            row = ""
            start = True

            for y in range(3):

                if not start:
                    row += "|"
                else:
                    start = False

                token = self._table[x * 3 + y]
                row += self.TOKEN_VERBOSE[token]

            print(row)

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
