class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows_len= len(grid)
        cols_len= len(grid[0])
        rows=[0]*rows_len
        cols=[0]*cols_len
        for i in range(rows_len):
            for j in range(cols_len):
                if grid[i][j]:
                    rows[i]+=1
                    cols[j]+=1
        ans=0
        for i in range(rows_len):
            for j in range(cols_len):
                if grid[i][j] and (rows[i]>1 or cols[j]>1):
                    ans+=1
        return ans