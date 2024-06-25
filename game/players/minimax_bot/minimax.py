from game.board import Board
from .tree import Node


class Minimax:
    def __init__(self, board: Board):
        self.token = 1
        print("loading minimax")
        self.board = board
        self.tree = Node(key="init", data={'board': str(self.board)})
        self._create_tree(board, self.tree)
        self._populate_rank(self.tree)
        print("minimax loaded!")

    def _create_tree(self, board: Board, node: Node, depth: int = 10):
        if depth <= 0:
            return

        moves = board.get_free_positions()
        for m in moves:
            turn = board.get_turn()
            board.add_token(m, turn)
            rank = None

            if board.is_winner(turn):
                rank = 1

                if self.token != turn:
                    rank = -1

            elif board.is_full():
                rank = 0

            node.add_child(m, {'rank': rank, 'board': str(self.board)})

            if rank is None:
                self._create_tree(board, node.children[m], depth - 1)

            board.undo()

    def _populate_rank(self, node, is_max: bool = True):
        if node.data.get('rank') is not None or not node.children:
            return

        if is_max:
            target = 1
            func = max
        else:
            target = -1
            func = min

        ranks = list(filter(lambda x: x is not None, map(lambda n: n.data.get('rank'), node.children.values())))
        # if any(map(lambda x: x == target, ranks)):
        #     node.data['rank'] = target
        #     return

        if len(ranks) == len(node.children):
            node.data['rank'] = func(ranks)

        for c in node.children.values():
            if c.data.get('rank') is None:
                self._populate_rank(c, not is_max)

                # if c.data.get('rank') == target:
                #     node.data['rank'] = target
                #     return

        ranks = list(filter(lambda x: x is not None, map(lambda n: n.data.get('rank'), node.children.values())))
        node.data['rank'] = func(ranks)

    def get_minimax_child(self, node: Node, token):
        rank = None
        _child = None

        if token == 1:
            func = max
        else:
            func = min

        for child in node.children.values():
            r = child.data.get('rank')

            if r is not None:
                if rank is None:
                    rank = r
                    _child = child

                elif func(r, rank) != rank:
                    rank = r
                    _child = child

        return _child
