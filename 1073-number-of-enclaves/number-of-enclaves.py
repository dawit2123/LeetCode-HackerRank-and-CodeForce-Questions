class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        number_of_land_cells=0
        row, col=len(grid), len(grid[0])
        def dfs(r, c):
            if min(r,c)<0 or r==row or c==col or grid[r][c]==0:
                return
            grid[r][c]=0
            nonlocal number_of_land_cells
            number_of_land_cells+=1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(row):
            for c in range(col):
                if r in [0, row-1] or c in [0, col-1]:
                    dfs(r,c)
        number_of_land_cells=0
        for r in range(row):
            for c in range(col):
                dfs(r,c)
        return number_of_land_cells