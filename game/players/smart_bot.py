from game.players.random_bot import RandomBot


class SmartBot(RandomBot):

    def next_move(self, board):

        for x in range(3):
            for y in range(3):
                if (x, y) not in board.table:
                    # check if bot wins
                    board.add_token(x, y, self.token)
                    if board.does_token_won(self.token):
                        return
                    else:
                        board.delete_token(x, y)

                    # check if bot looses
                    board.add_token(x, y, self.opponent_token)
                    if board.does_token_won(self.opponent_token):
                        board.delete_token(x, y)
                        board.add_token(x, y, self.token)
                        return
                    else:
                        board.delete_token(x, y)


        return super(SmartBot, self).next_move(board)