from game.game import TicTacToeGame
from game.players import MinimaxBot, Human, RuleBot

if __name__ == '__main__':
    game = TicTacToeGame(players=[Human, MinimaxBot], monitor=True, fast_mode=False, debug=True)
    game.run_loop()

    print(f'Winner: {game.winner}')
    game.board.print()
