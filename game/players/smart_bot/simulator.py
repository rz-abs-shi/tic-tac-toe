from game.game import TicTacToeGame
from game.players import SmartBot, RandomBot
from game.players.rule_bot import RuleBot


def success_rates(player1, player2, n: int = 1000) -> tuple:
    player1_won = 0
    player2_won = 0

    for i in range(n):
        game = TicTacToeGame(players=[player1, player2], monitor=False)
        game.run_loop()

        if game.winner:
            if game.winner.token == 1:
                player1_won += 1

            elif game.winner.token == 2:
                player2_won += 1

    return float(player1_won) / n, float(player2_won) / n


if __name__ == '__main__':
    rates = success_rates(RuleBot, RuleBot)
    print(rates)
