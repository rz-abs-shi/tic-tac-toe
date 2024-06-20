from game.game import TicTacToeGame
from game.players import Human, SmartBot

if __name__ == '__main__':
    game = TicTacToeGame(players=[Human, SmartBot])
    game.run_loop()

    print(game.winner)
