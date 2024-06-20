from game.game import TicTacToeGame
from game.players import SmartBot

if __name__ == '__main__':
    game = TicTacToeGame(players=[SmartBot, SmartBot], monitor=False)
    game.run_loop()

    print(f'Winner: {game.winner}')
    game.board.print()
