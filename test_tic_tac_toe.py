import unittest
from tic_tac_toe import check_win, check_draw

class TestTicTacToe(unittest.TestCase):

    def test_check_win(self):
        # Test rows
        board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertTrue(check_win(board, "X"))
        # Test columns
        board = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
        self.assertTrue(check_win(board, "O"))
        # Test diagonals
        board = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertTrue(check_win(board, "X"))
        board = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]
        self.assertTrue(check_win(board, "O"))
        # Test no win
        board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertFalse(check_win(board, "X"))
        self.assertFalse(check_win(board, "O"))

    def test_check_draw(self):
        # Test draw
        board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertTrue(check_draw(board))
        # Test not a draw
        board = [["X", "O", "X"], ["O", " ", "O"], ["O", "X", "O"]]
        self.assertFalse(check_draw(board))

if __name__ == '__main__':
    unittest.main()
