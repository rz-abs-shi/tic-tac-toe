from game.game import TicTacToeGame
from game.players import MinimaxBot, Human, RuleBot, RandomBot
from collections import defaultdict
from game.analyzer import analyze_player


if __name__ == '__main__':
    # game = TicTacToeGame(players=[RuleBot, MinimaxBot], monitor=True, fast_mode=False, debug=True)
    # game.run_loop()

    # print(f'Winner: {game.winner}')
    # game.board.print()
    analyze_player(RandomBot, MinimaxBot, 100)

