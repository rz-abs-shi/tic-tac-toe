
class IPlayer:
    is_bot = True

    def __init__(self, token):
        self.token = token

    def _next_move(self, board):
        raise NotImplementedError

    def next_move(self, board):
        self._next_move(board)

    def __str__(self):
        return self.token
