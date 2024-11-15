class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col= len(grid2), len(grid2[0])
        visit=set()
        def dfs(r,c):
            if min(r,c)<0 or r==row or c==col  or (r,c) in visit or grid2[r][c]==0 :
                return True
            res=True
            visit.add((r,c))
            if grid1[r][c]==0:
                res=False
            res=dfs(r+1, c) and res
            res= dfs(r-1, c) and res
            res= dfs(r, c+1) and res
            res= dfs(r, c-1) and res
            return res
        count=0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    count+=1
        return count