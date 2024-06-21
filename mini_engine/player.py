
class IPlayer:
    def __init__(self, token: int, fast_mode: bool = True, debug: bool = False):
        self.token = token
        self.fast_mode = fast_mode
        self.debug = debug

    def get_move(self, board):
        raise NotImplementedError

    def __str__(self):
        return f"Player {self.token}"

    def get_opponent_token(self):
        return 3 - self.token
