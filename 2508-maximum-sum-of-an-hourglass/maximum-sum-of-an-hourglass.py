class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
      
        max_hourglass_sum = 0
      
        for row in range(1, num_rows - 1):
            for col in range(1, num_columns - 1):
                hourglass_sum = (
                    grid[row - 1][col - 1] +
                    grid[row - 1][col] +
                    grid[row - 1][col + 1] +
                    grid[row][col] + 
                    grid[row + 1][col - 1] +
                    grid[row + 1][col] +
                    grid[row + 1][col + 1]
                )
              
                max_hourglass_sum = max(max_hourglass_sum, hourglass_sum)
              
        return max_hourglass_sum