# Tic-Tac-Toe game in Python

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (i.e., a tie)
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        # Get the current player's move
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

        # Ensure the cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This cell is already taken! Try again.")
            continue

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
