def sudoku_solve(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            subgrid_index = (i // 3) * 3 + j // 3
            if num in rows[i] or num in cols[j] or num in subgrids[subgrid_index]:
                return False
            rows[i].add(num)
            cols[j].add(num)
            subgrids[subgrid_index].add(num)

    sudoku = [['.' for _ in range(9)] for _ in range(9)]

    # Arrays to store possible values for each row, column, and box
    row_vals = [0] * 9
    col_vals = [0] * 9
    box_vals = [[0] * 3 for _ in range(3)]

    # Set a bit corresponding to the value in the bit mask
    def set_bit(mask, val):
        return mask | (1 << val)

    # Clear a bit corresponding to the value in the bit mask
    def clear_bit(mask, val):
        return mask & ~(1 << val)

    # Check if a bit corresponding to the value is set in the bit mask
    def check_bit(mask, val):
        return mask & (1 << val)

    # Find possible values for the cell (row, col)
    def possible_values(row, col):
        return ~(row_vals[row] | col_vals[col] | box_vals[row // 3][col // 3])

    # Solve Sudoku recursively
    def solve(row, col):
        if row == 9:
            return True
        if col == 9:
            return solve(row + 1, 0)
        if sudoku[row][col] == '.':
            mask = possible_values(row, col)
            for val in range(9):
                if check_bit(mask, val):
                    sudoku[row][col] = str(1 + val)
                    row_vals[row] = set_bit(row_vals[row], val)
                    col_vals[col] = set_bit(col_vals[col], val)
                    box_vals[row // 3][col // 3] = set_bit(box_vals[row // 3][col // 3], val)
                    if solve(row, col + 1):
                        return True
                    sudoku[row][col] = '.'
                    row_vals[row] = clear_bit(row_vals[row], val)
                    col_vals[col] = clear_bit(col_vals[col], val)
                    box_vals[row // 3][col // 3] = clear_bit(box_vals[row // 3][col // 3], val)
            return False
        return solve(row, col + 1)

    for i in range(9):
        row_input = board[i]
        for j in range(9):
            sudoku[i][j] = row_input[j]
            if sudoku[i][j] != '.':
                val = int(sudoku[i][j]) - 1
                row_vals[i] = set_bit(row_vals[i], val)
                col_vals[j] = set_bit(col_vals[j], val)
                box_vals[i // 3][j // 3] = set_bit(box_vals[i // 3][j // 3], val)
    if solve(0,0):
        return sudoku