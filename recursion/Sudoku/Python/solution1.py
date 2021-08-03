# time : O(1)
# space : O(1)

def solve_sudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row, col, board):
    current_row = row
    current_col = col

    if current_col == len(board[row]):
        current_row += 1
        current_col = 0
        if current_row == len(board):
            return True

    if board[current_row][current_col] == 0:
        return try_digits_at_position(current_row, current_col, board)

    return solve_partial_sudoku(current_row, current_col+1, board)


def try_digits_at_position(row, col, board):
    for digit in range(1, 10):

        if is_valid_at_postion(digit, row, col, board):
            board[row][col] = digit

            if solve_partial_sudoku(row, col + 1, board):
                return True

    board[row][col] = 0
    return False


def is_valid_at_postion(value, row, col, board):
    row_is_valid = value not in board[row]
    col_is_valid = value not in map(lambda r: r[col], board)

    if not row_is_valid or not col_is_valid:
        return False

    subgrid_row_start = row // 3
    subgrid_col_start = col // 3

    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = subgrid_row_start * 3 + row_idx
            col_to_check = subgrid_col_start * 3 + col_idx
            existing_value = board[row_to_check][col_to_check]

            if existing_value == value:
                return False

    return True


board = [[0, 0, 0, 9, 0, 2, 7, 3, 8],
         [0, 6, 0, 0, 0, 5, 0, 0, 9],
         [8, 2, 9, 3, 0, 0, 6, 0, 1],
         [0, 0, 1, 0, 0, 6, 0, 8, 2],
         [0, 9, 3, 0, 1, 0, 4, 0, 5],
         [0, 8, 0, 7, 0, 0, 9, 1, 0],
         [9, 0, 0, 0, 0, 7, 0, 0, 0],
         [0, 3, 8, 6, 0, 0, 5, 0, 0],
         [0, 0, 0, 5, 0, 1, 8, 9, 4]]

print(solve_sudoku(board))

output = [[5, 1, 4, 9, 6, 2, 7, 3, 8],
          [3, 6, 7, 1, 8, 5, 2, 4, 9],
          [8, 2, 9, 3, 7, 4, 6, 5, 1],
          [7, 5, 1, 4, 9, 6, 3, 8, 2],
          [6, 9, 3, 2, 1, 8, 4, 7, 5],
          [4, 8, 2, 7, 5, 3, 9, 1, 6],
          [9, 4, 5, 8, 2, 7, 1, 6, 3],
          [1, 3, 8, 6, 4, 9, 5, 2, 7],
          [2, 7, 6, 5, 3, 1, 8, 9, 4]]
