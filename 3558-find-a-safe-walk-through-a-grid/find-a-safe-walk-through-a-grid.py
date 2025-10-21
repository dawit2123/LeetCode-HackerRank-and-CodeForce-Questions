class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        memo = {}
        def dfs(x,y,ans):
            if x<0 or x>=m or y>=n or y<0 or vis[x][y]==1 or ans>=h:
                return float('inf')

            if x==m-1 and y==n-1:
                return ans+grid[x][y]

            if (x,y,ans) in memo:
                return memo[(x,y,ans)]

            vis[x][y] = 1
            
            memo[(x,y,ans)] = min(dfs(x+1,y,ans+grid[x][y]),dfs(x-1,y,ans+grid[x][y]),dfs(x,y+1,ans+grid[x][y]),dfs(x,y-1,ans+grid[x][y]))
            vis[x][y] = 0
            return memo[(x,y,ans)]
        a = dfs(0,0,0)
        return a-h<0
