# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh=0,0
        q=deque()
        row, col= len(grid), len(grid[0])
        # iterating over and counting the fresh
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        directions=[(1,0), (-1, 0), (0, 1), (0,-1)]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    row1, col1= r+dr, c+dc
                    if row1==row or col1==col or min(row1, col1)<0 or grid[row1][col1]!=1:
                        continue
                    grid[row1][col1]=2
                    fresh-=1
                    q.append((row1,col1))
            time+=1
        return time if fresh==0 else -1