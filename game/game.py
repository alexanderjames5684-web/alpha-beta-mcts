"""Connect Four rules and a two-player terminal interface.

Agents use columns 0-6. The terminal labels them 1-7.
Board values: 0 = empty, 1 = X, 2 = O. Row 0 is the top.
"""


class ConnectFour:
    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        self.board = [[0 for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self.current_player = 1

    def legal_moves(self):
        """Return available columns (0-6), or [] when the game is over."""
        if self.is_terminal():
            return []
        return [column for column in range(self.COLUMNS)
                if self.board[0][column] == 0]

    def apply_move(self, column):
        """Modify this board and switch players after a valid move.

        Invalid moves raise ValueError without changing the board or turn.
        current_player always identifies the next player, even after a win.
        """
        if self.is_terminal():
            raise ValueError("The game is over. Start a new game.")
        if type(column) is not int or not 0 <= column < self.COLUMNS:
            raise ValueError("Internal column must be an integer from 0 to 6.")
        if self.board[0][column] != 0:
            raise ValueError("That column is full. Choose another column.")

        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.current_player = 3 - self.current_player
                return

    def _check_direction(self, row_step, column_step):
        """Find four matching pieces along one direction."""
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                player = self.board[row][column]
                if player == 0:
                    continue

                # Check the end of the group before reading its cells.
                end_row = row + 3 * row_step
                end_column = column + 3 * column_step
                if not (0 <= end_row < self.ROWS
                        and 0 <= end_column < self.COLUMNS):
                    continue

                if all(self.board[row + i * row_step][column + i * column_step]
                       == player for i in range(1, 4)):
                    return player
        return None

    def check_horizontal_win(self):
        """Return the horizontal winner (1 or 2), otherwise None."""
        return self._check_direction(0, 1)

    def check_vertical_win(self):
        """Return the vertical winner (1 or 2), otherwise None."""
        return self._check_direction(1, 0)

    def check_diagonal_win(self):
        """Check both diagonal slopes and return a winner or None."""
        return self._check_direction(1, 1) or self._check_direction(1, -1)

    def get_winner(self):
        """Return 1 or 2 for a win, 0 for a draw, or None if ongoing."""
        winner = (self.check_horizontal_win()
                  or self.check_vertical_win()
                  or self.check_diagonal_win())
        if winner is not None:
            return winner
        if all(cell != 0 for row in self.board for cell in row):
            return 0
        return None

    def is_draw(self):
        """A draw is a full board without a winner."""
        return self.get_winner() == 0

    def is_terminal(self):
        """Return True when either player wins or the board is a draw."""
        return self.get_winner() is not None

    def clone(self):
        """Return an independent game copy for hypothetical agent moves."""
        copied_game = ConnectFour()
        copied_game.board = [row[:] for row in self.board]
        copied_game.current_player = self.current_player
        return copied_game

    def display(self):
        """Print human column labels and piece symbols."""
        symbols = {0: ".", 1: "X", 2: "O"}
        print("\n  1 2 3 4 5 6 7")
        for row in self.board:
            print("| " + " ".join(symbols[cell] for cell in row) + " |")
        print()


def main():
    game = ConnectFour()
    print("Connect Four - Player 1: X, Player 2: O")
    print("Choose a column from 1 to 7. Enter q to quit.")
    game.display()

    while not game.is_terminal():
        try:
            choice = input(f"Player {game.current_player}, choose a column (1-7): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGame closed.")
            return
        if choice.strip().lower() == "q":
            print("Game closed.")
            return

        try:
            column = int(choice)
        except ValueError:
            print("Enter a whole number from 1 to 7, or q to quit.")
            continue
        if not 1 <= column <= game.COLUMNS:
            print("Choose a column from 1 to 7.")
            continue
        try:
            game.apply_move(column - 1)
        except ValueError as error:
            print(error)
            continue
        game.display()

    if game.is_draw():
        print("Draw! The board is full.")
    else:
        print(f"Player {game.get_winner()} wins!")


if __name__ == "__main__":
    main()
