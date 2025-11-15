# Tic-Tac-Toe Game

def print_board(board):
    """Prints the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    """Checks if a player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all([cell != " " for row in board for cell in row])

def main():
    """Main function to run the tic-tac-toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid input. Row and column must be between 0 and 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken!")

if __name__ == "__main__":
    main()
