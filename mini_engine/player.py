
class IPlayer:
    is_bot = True

    def __init__(self, token, opponent_token):
        self.token = token
        self.opponent_token = opponent_token

    def next_move(self, board):
        pass