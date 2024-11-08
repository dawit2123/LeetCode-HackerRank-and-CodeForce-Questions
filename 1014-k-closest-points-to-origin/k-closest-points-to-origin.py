class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            heapq.heappush(heap, ((abs(point[0]**2) + abs(point[1]**2)), point))
        res=[]
        for i in range(k):
            res.append((heapq.heappop(heap))[1])
        return res