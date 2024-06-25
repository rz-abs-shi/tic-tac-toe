from game.game import TicTacToeGame
from game.players import MinimaxBot
from game.players.rule_bot import RuleBot


def success_rates(player1, player2, n: int = 1000) -> tuple:
    player1_won = 0
    player2_won = 0

    wins = {1: [], 2: []}

    for i in range(n):
        game = TicTacToeGame(players=[player1, player2], monitor=False)
        game.run_loop()

        if game.winner:
            if game.winner.token == 1:
                player1_won += 1

                wins[1].append(game.board)

            elif game.winner.token == 2:
                player2_won += 1
                wins[2].append(game.board)

    return float(player1_won) / n, float(player2_won) / n, wins


if __name__ == '__main__':
    rate1, rate2, wins = success_rates(MinimaxBot, MinimaxBot)
    print(rate1, rate2)

    # print(wins[2][0].get_str(True))
