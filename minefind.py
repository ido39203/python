import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(rows, cols):
    board = [["0" for _ in range(cols)] for _ in range(rows)]
    return board

def place_mines(board, num_mines):
    num_rows = len(board)
    num_cols = len(board[0])
    for _ in range(num_mines):
        row, col = random.randint(0, num_rows - 1), random.randint(0, num_cols - 1)
        while board[row][col] == "*":
            row, col = random.randint(0, num_rows - 1), random.randint(0, num_cols - 1)
        board[row][col] = "*"

def count_adjacent_mines(board, row, col):
    num_rows = len(board)
    num_cols = len(board[0])
    if board[row][col] == "*":
        return "*"
    count = 0
    for i in range(max(0, row-1), min(num_rows, row+2)):
        for j in range(max(0, col-1), min(num_cols, col+2)):
            if board[i][j] == "*":
                count += 1
    return str(count)

def reveal_square(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] != "0":
        return
    num_rows = len(board)
    num_cols = len(board[0])
    for i in range(max(0, row-1), min(num_rows, row+2)):
        for j in range(max(0, col-1), min(num_cols, col+2)):
            reveal_square(board, revealed, i, j)

def play_game(rows, cols, num_mines):
    board = create_board(rows, cols)
    place_mines(board, num_mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    while True:
        print_board(board)
        row = int(input("Enter row (0-indexed): "))
        col = int(input("Enter col (0-indexed): "))
        if board[row][col] == "*":
            print("You lose!")
            print_board(board)
            break
        reveal_square(board, revealed, row, col)
        if all(all(row) for row in revealed):
            print("You win!")
            print_board(board)
            break

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))
    num_mines = int(input("Enter number of mines: "))
    play_game(rows, cols, num_mines)
