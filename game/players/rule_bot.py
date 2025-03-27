import random
import time

from game.board import Board
from mini_engine.player import IPlayer


class RuleBot(IPlayer):
    name = 'rule'
    
    def get_winner_moves(self, board: Board, next_token: int):
        moves = []
        new_board = board.clone()

        for pos in new_board.get_free_positions():
            new_board.add_token(pos, next_token)

            if new_board.is_winner(next_token):
                moves.append(pos)

            new_board.undo()

        return moves

    def get_move(self, board):
        if not self.fast_mode:
            print("Bot is thinking")
            time.sleep(2)

        # First select wining moves

        winning_moves = self.get_winner_moves(board, self.token)

        if self.debug:
            print(f"winning_moves: {winning_moves}")

        if winning_moves:
            return winning_moves[0]

        # Get non loosing moves

        allowed_pos = []
        new_board = board.clone()
        for pos in new_board.get_free_positions():
            new_board.add_token(pos, self.token)
            if not self.get_winner_moves(new_board, self.get_opponent_token()):
                allowed_pos.append(pos)
            new_board.undo()

        if self.debug:
            print(f"allowed_pos: {allowed_pos}")

        if allowed_pos:
            # Select center if not loosing!
            if 4 in allowed_pos:
                return 4

            return random.choice(allowed_pos)

        # Random select!
        free_pos = board.get_free_positions()
        if self.debug:
            print(f"free_pos: {free_pos}")

        return random.choice(free_pos)
