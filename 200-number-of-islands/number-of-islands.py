class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS= len(grid), len(grid[0])
        islands=0
        visit=set()
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col= q.popleft()
                directions=[[1,0], [-1, 0], [0,1], [0,-1]]
                for x, y in directions:
                    r,c=row+x, col+y
                    if r in range(ROWS) and c in range(COLS) and grid[r][c]=="1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands