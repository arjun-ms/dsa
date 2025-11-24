class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Check if first row has any zero
        first_row_zero = False
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column has any zero
        first_col_zero = False
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column to mark zero rows/columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out rows based on markers (except first row)
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
                    
        # Zero out columns based on markers (except first column)
        for j in range(1,cols):
            if matrix[0][j]==0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Zero entire first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero entire first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


##############################################
##############################################


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_set, cols_set = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_set.add(row)
                    cols_set.add(col)
        
        for row in range(rows):
            for col in range(cols):
                if row in rows_set or col in cols_set:
                    matrix[row][col] = 0
                    

            
