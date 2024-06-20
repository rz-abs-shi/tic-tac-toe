from game.players.random_bot import RandomBot


class SmartBot(RandomBot):

    def _next_move(self, board):
        # check if bot wins
        return super(SmartBot, self)._next_move(board)
