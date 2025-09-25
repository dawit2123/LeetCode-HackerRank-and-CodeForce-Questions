class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        dp = [[0] * (num_rows + 1) for _ in range(num_rows + 1)]
        for row in range(num_rows - 1, -1, -1):
            for col in range(row + 1):
                dp[row][col] = min(dp[row + 1][col], dp[row + 1][col + 1]) + triangle[row][col]      
        return dp[0][0]