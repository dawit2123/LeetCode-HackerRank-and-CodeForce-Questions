from collections import defaultdict
import heapq
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        diagonal=defaultdict(list)
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                key=i-j
                if i-j<0:
                    heapq.heappush(diagonal[key], grid[i][j])
                else:
                    heapq.heappush(diagonal[key], -1*grid[i][j])
        for i in range(n):
            for j in range(m):
                key=i-j
                if key<0:
                    value=heapq.heappop(diagonal[key])
                    grid[i][j]=value
                else:
                    value= -1*(heapq.heappop(diagonal[key]))
                    grid[i][j]=value
        return grid