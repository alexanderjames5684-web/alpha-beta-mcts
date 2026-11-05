"""Run from the repository root with: python -m unittest -v test_game"""

import random
import unittest

from game.game import ConnectFour


class GameTests(unittest.TestCase):
    def test_empty_board_and_independent_rows(self):
        game = ConnectFour()
        self.assertEqual(game.legal_moves(), list(range(7)))
        self.assertIsNone(game.get_winner())
        self.assertFalse(game.is_terminal())
        game.board[5][0] = 1
        self.assertEqual(game.board[4][0], 0)

    def test_gravity_turns_and_full_column(self):
        game = ConnectFour()
        for _ in range(6):
            game.apply_move(0)
        self.assertEqual([row[0] for row in game.board], [2, 1, 2, 1, 2, 1])
        self.assertNotIn(0, game.legal_moves())
        before = game.clone()
        for column in [0, -1, 7, 1.5, "2", True, None]:
            with self.assertRaises(ValueError):
                game.apply_move(column)
            self.assertEqual(game.board, before.board)
            self.assertEqual(game.current_player, before.current_player)

    def test_every_four_cell_window(self):
        # Exhaustively cover all 69 possible winning windows for both players.
        count = 0
        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            for row in range(6):
                for column in range(7):
                    if not (0 <= row + 3 * dr < 6 and 0 <= column + 3 * dc < 7):
                        continue
                    count += 1
                    for player in [1, 2]:
                        game = ConnectFour()
                        for i in range(4):
                            game.board[row + i * dr][column + i * dc] = player
                        self.assertEqual(game.get_winner(), player)
                        self.assertTrue(game.is_terminal())
                        self.assertEqual(game.legal_moves(), [])
                        game.board[row + 2 * dr][column + 2 * dc] = 0
                        self.assertIsNone(game.get_winner())
        self.assertEqual(count, 69)

    def test_horizontal_and_vertical_move_sequences(self):
        for moves in [[0, 6, 1, 6, 2, 5, 3], [0, 1, 0, 1, 0, 1, 0]]:
            game = ConnectFour()
            for move in moves:
                game.apply_move(move)
            self.assertEqual(game.get_winner(), 1)
            before = game.clone()
            with self.assertRaises(ValueError):
                game.apply_move(2)
            self.assertEqual(game.board, before.board)

    def test_clone_is_independent(self):
        game = ConnectFour()
        game.apply_move(3)
        copy = game.clone()
        self.assertEqual(copy.current_player, 2)
        copy.apply_move(3)
        self.assertEqual(game.board[4][3], 0)
        self.assertEqual(game.current_player, 2)
        self.assertEqual(copy.board[4][3], 2)

    def test_draw_and_full_board_win_precedence(self):
        game = ConnectFour()
        game.board = [[1, 1, 2, 2, 1, 1, 2], [2, 2, 1, 1, 2, 2, 1]] * 3
        game.board = [row[:] for row in game.board]
        self.assertEqual(game.get_winner(), 0)
        self.assertTrue(game.is_draw())
        self.assertTrue(game.is_terminal())
        self.assertEqual(game.legal_moves(), [])
        game.board[0][:4] = [1, 1, 1, 1]
        self.assertEqual(game.get_winner(), 1)
        self.assertFalse(game.is_draw())

    def test_random_games_against_independent_winner_check(self):
        def reference(board):
            for player in (1, 2):
                for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                    for r in range(6):
                        for c in range(7):
                            cells = [(r + i * dr, c + i * dc) for i in range(4)]
                            if all(0 <= y < 6 and 0 <= x < 7
                                   and board[y][x] == player for y, x in cells):
                                return player
            return 0 if all(all(row) for row in board) else None

        rng = random.Random(42)
        for _ in range(100):
            game = ConnectFour()
            while not game.is_terminal():
                game.apply_move(rng.choice(game.legal_moves()))
                self.assertEqual(game.get_winner(), reference(game.board))


if __name__ == "__main__":
    unittest.main()
