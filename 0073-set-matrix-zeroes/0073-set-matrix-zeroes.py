from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and columns using first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero marked rows
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Zero marked columns
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0