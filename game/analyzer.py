from game.game import TicTacToeGame
from collections import defaultdict
import random


def analyze_player(player1, player2, n: int = 100):
    winners = defaultdict(int)
    players = [player1, player2]

    for i in range(n):
        random.shuffle(players)
        game = TicTacToeGame(players=players, monitor=False, fast_mode=True, debug=False)
        game.run_loop()
        w = game.winner
        winners[w and w.name] += 1

    for p in [player1, player2]:
        print(f'Player {p.name} winned: {round(winners.get(p.name, 0) * 100 / n, 2)}%')

    print(f'Game drawed: {round(winners.get(None, 0) * 100 / n, 2)}%')


    return winners
