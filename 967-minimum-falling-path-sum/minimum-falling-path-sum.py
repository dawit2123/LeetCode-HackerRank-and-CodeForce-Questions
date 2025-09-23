from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(n):
                up = matrix[i][j] + dp[i - 1][j]
                ld = matrix[i][j] + dp[i - 1][j + 1] if j < n - 1 else float('inf')
                rd = matrix[i][j] + dp[i - 1][j - 1] if j > 0 else float('inf')

                dp[i][j] = min(up, ld, rd)

        return min(dp[n - 1])