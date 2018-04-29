from mini_engine.player import IPlayer


class Human(IPlayer):

    def next_move(self, board):
        input_got = False
        while not input_got:
            try:
                inp = input("Please Enter x,y: ").split(',')

                if len(inp) != 2:
                    continue

                x = int(inp[0])
                y = int(inp[1])

                if board.add_token(x, y, self.token):
                    input_got = True
            except:
                continue
