class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left_min=float('inf')
        right_max=0
        upper_min=float('inf')
        lower_max=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    upper_min= min(upper_min, i)
                    lower_max= max(lower_max, i)
                    left_min= min(left_min, j)
                    right_max= max(right_max, j)
        return (lower_max-upper_min+1)*(right_max-left_min+1)