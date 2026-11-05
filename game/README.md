# Connect Four environment

Run from the repository root:

```bash
python game/game.py
python -m unittest -v test_game
```

Python 3 is sufficient. No third-party packages are required.

## Board and move conventions

The board has six rows and seven columns. Row 0 is the top.
Values are 0 for empty, 1 for X, and 2 for O.
Agent moves use column indices 0 through 6. Terminal input uses 1 through 7.

## Agent interface

| Method | Result or behavior |
| --- | --- |
| legal_moves() | Available columns, or an empty list when the game ends |
| apply_move(column) | Changes this board and switches players. Invalid moves raise ValueError without changing state |
| get_winner() | 1 or 2 for a winner, 0 for a draw, None while ongoing |
| is_terminal() | True after a win or draw |
| is_draw() | True for a full board without a winner |
| clone() | Independent copy of the board and current player |
| display() | Prints the current board |

current_player identifies the next player, including after a terminal move.
Always use get_winner() to determine who won. Check get_winner() is not None rather than truthiness, because a draw returns 0.

## Search example

```python
from game.game import ConnectFour

game = ConnectFour()
for move in game.legal_moves():
    child = game.clone()
    child.apply_move(move)
    # Evaluate child without changing game.
    print(move, child.get_winner())
```

The environment detects horizontal, vertical, and both diagonal wins. A winning line takes precedence over a full-board draw.
The tournament runner should stop when is_terminal() returns True.
