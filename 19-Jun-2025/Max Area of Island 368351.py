# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL= len(grid), len(grid[0])
        max_area=0
        def dfs(r,c):
            if min(r,c)<0 or r==ROW or c==COL or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return (1+ dfs(r+1,c)+ dfs(r-1,c)+dfs(r,c+1)+ dfs(r, c-1))
        for r in range (ROW):
            for c in range(COL):
                max_area=max(max_area, dfs(r,c))
        return max_area