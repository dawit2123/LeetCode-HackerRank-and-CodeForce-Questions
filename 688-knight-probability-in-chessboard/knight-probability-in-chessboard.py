class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        move = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                 (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1.0
        
        for step in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for dr, dc in move:
                        x, y = i + dr, j + dc
                        if 0 <= x < n and 0 <= y < n:
                            dp[step][i][j] += dp[step - 1][x][y] / 8.0
        
        return dp[k][row][column]