# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_len = len(points)
        adjacents = {i: [] for i in range(points_len)}

        for i in range(points_len):
            x1, y1 = points[i]
            for j in range(i + 1, points_len):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adjacents[i].append([j, weight])
                adjacents[j].append([i, weight])
        
        res = 0
        visit = set()
        min_heap = [[0, 0]]  
        
        while len(visit) < points_len:
            cost, node = heapq.heappop(min_heap)
            
            if node in visit:
                continue
            visit.add(node)
            res += cost
            
            for j, cost2 in adjacents[node]:
                if j not in visit:
                    heapq.heappush(min_heap, [cost2, j]) 
        return res
