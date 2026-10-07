class AlphaBetaAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def choose_move(self, game):
        moves = game.legal_moves()

        if not moves:
            return None

        return moves[0]

    def evaluate(self, game, player):
        """
        Give the current board a numerical score from the perspective
        of the specified player.

        Positive scores favor the player.
        Negative scores favor the opponent.

        This evaluation function will eventually consider several
        Connect Four strategies. For now, it only evaluates control
        of the center column.
        """

        # In this game, players are represented by 1 and 2.
        # Subtracting the current player from 3 gives us the other player.
        opponent = 3 - player

        # Connect Four has 7 columns, so integer division gives us
        # column index 3, which is the center column.
        center_column = game.COLUMNS // 2

        # Start with a neutral board score.
        score = 0

        # Examine every space in the center column.
        for row in range(game.ROWS):

            # Reward the player for occupying the center.
            if game.board[row][center_column] == player:
                score += 3

            # Penalize the player when the opponent controls the center.
            elif game.board[row][center_column] == opponent:
                score -= 3

        # Examine every horizontal group of four spaces on the board.
        for row in range(game.ROWS):
            for column in range(game.COLUMNS - 3):

                # Take four consecutive spaces from this row.
                window = game.board[row][column:column + 4]

                # Add this window's value to the overall board score.
                score += self._score_window(window, player)

        # Examine every vertical group of four spaces on the board.
        for column in range(game.COLUMNS):
            for row in range(game.ROWS - 3):

                # Build a four-space vertical window from top to bottom.
                window = [
                    game.board[row + offset][column]
                    for offset in range(4)
                ]

                # Add this window's value to the overall board score.
                score += self._score_window(window, player)

        # Examine every downward-right diagonal group of four spaces.
        for row in range(game.ROWS - 3):
            for column in range(game.COLUMNS - 3):

                # Build a four-space diagonal window.
                window = [
                    game.board[row + offset][column + offset]
                    for offset in range(4)
                ]

                # Add this window's value to the overall board score.
                score += self._score_window(window, player)

        # Examine every upward-right diagonal group of four spaces.
        for row in range(3, game.ROWS):
            for column in range(game.COLUMNS - 3):

                # Build a four-space diagonal window.
                window = [
                    game.board[row - offset][column + offset]
                    for offset in range(4)
                ]

                # Add this window's value to the overall board score.
                score += self._score_window(window, player)

        return score

    def _score_window(self, window, player):
        """
        Evaluate a group of four board spaces.

        A "window" is any four consecutive spaces that could potentially
        form a Connect Four: horizontal, vertical, or diagonal.

        This helper will eventually reward useful patterns for the player
        and penalize dangerous patterns created by the opponent.
        """

        # Players are represented by 1 and 2, so this gives us
        # the player on the opposite side.
        opponent = 3 - player

        # Count how many spaces in this group of four belong to
        # the player, the opponent, or are still empty.
        player_count = window.count(player)
        opponent_count = window.count(opponent)
        empty_count = window.count(0)

        # Start this four-space window with a neutral score.
        score = 0

        # A completed Connect Four is extremely valuable, so give it
        # a much larger score than any partial pattern.
        if player_count == 4:
            score += 100

        # Three pieces and one empty space means the player is one move
        # away from completing Connect Four, so reward this pattern.
        elif player_count == 3 and empty_count == 1:
            score += 5

        # If the opponent has three pieces and one empty space, they are
        # one move away from winning. Penalize this pattern so the agent
        # will prefer moves that block the threat.
        if opponent_count == 3 and empty_count == 1:
            score -= 6

        return score