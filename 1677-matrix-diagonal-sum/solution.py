from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]             # Primary diagonal
            total += mat[i][n - 1 - i]     # Secondary diagonal

        if n % 2 == 1:
            # Subtract the center element once (it was added twice)
            total -= mat[n // 2][n // 2]

        return total

    
