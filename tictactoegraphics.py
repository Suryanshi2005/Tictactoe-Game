import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables for the game
current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check if there is a winner
def check_winner():
    global current_player
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check if it's a tie
def check_tie():
    for row in board:
        if " " in row:
            return False
    return True

# Function to handle button clicks
def handle_click(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player
        buttons[row][col]["state"] = "disabled"
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This spot is already taken!")

# Function to reset the game
def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = " "
            buttons[row][col]["state"] = "normal"

# Create the grid of buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24), 
                                      command=lambda r=row, c=col: handle_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Start the main loop of the application
root.mainloop()
