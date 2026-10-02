"""Connect Four starter: board display, piece placement, and alternating turns."""


from matplotlib.pylab import rint


class ConnectFour:
    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        # Each row is a separate list. Row 0 is the top of the board.
        self.board = [[0 for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self.current_player = 1

    def legal_moves(self):
        """Return available columns using internal column numbers 0 through 6."""
        return [
            column for column in range(self.COLUMNS)
            if self.board[0][column] == 0
        ]

    def apply_move(self, column):
        """Drop a piece into a column, then switch players."""
        if type(column) is not int or not 0 <= column < self.COLUMNS:
            raise ValueError("Choose a column from 1 to 7.")
        if self.board[0][column] != 0:
            raise ValueError("That column is full. Choose another column.")

        # Search upward from the bottom for the first empty space.
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                self.current_player = 3 - self.current_player
                return

    def check_horizontal_win(self):
    # Check for a horizontal win on the board.

        for row in range(self.ROWS):
            for column in range(self.COLUMNS-3):
                player=self.board[row][column]

                if player == 0:
                    continue

                if (
                    self.board[row][column+1] == player and
                    self.board[row][column+2] == player and
                    self.board[row][column+3] == player
                ):
                    return player
        return None

    def display(self):
        """Print the board with column labels 1 through 7 for human players."""
        symbols = {0: ".", 1: "X", 2: "O"}
        print("\n  1 2 3 4 5 6 7")
        for row in self.board:
            print("| " + " ".join(symbols[cell] for cell in row) + " |")
        print()

def main():
    game = ConnectFour()
    print("Connect Four starter — Player 1: X, Player 2: O")
    print("Only Horizontal wins are checked. Vertical and Diagonal wins are not checked yet. Enter q to quit.")
    game.display()

    while game.legal_moves():
        try:
            choice = input(f"Player {game.current_player}, choose a column (1-7): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGame closed.")
            return

        if choice.strip().lower() == "q":
            print("Game closed.")
            return

        try:
            # Human column 1 corresponds to internal column 0.
            game.apply_move(int(choice) - 1)
        except ValueError as error:
            if not choice.strip().lstrip("+-").isdigit():
                print("Enter a whole number from 1 to 7, or q to quit.")
            else:
                print(error)
            continue
        game.display()
        
        # Check for a horizontal win after each move.
        winner = game.check_horizontal_win()
        if winner is not None:
            print(f"Player {winner} wins!")
            return
       
  

    print("The board is full. This starter does not evaluate wins or draws yet.")


if __name__ == "__main__":
    main()
