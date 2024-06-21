def sudoku(puzzle):
    def is_valid(row, col, num):
        # Check if the number is already present in the row
        for i in range(9):
            if puzzle[row][i] == num:
                return False

        # Check if the number is already present in the column
        for i in range(9):
            if puzzle[i][col] == num:
                return False

        # Check if the number is already present in the 3x3 grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if puzzle[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            puzzle[row][col] = num
                            if solve():
                                return True
                            puzzle[row][col] = 0
                    return False
        return True

    solve()
    return puzzle
