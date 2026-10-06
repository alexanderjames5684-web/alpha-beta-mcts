class AlphaBetaAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def choose_move(self, game):
        moves = game.legal_moves()

        if not moves:
            return None

        return moves[0]