class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        max_heap=[-1*weight for weight in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            heaviest1=max_heap[0]
            heapq.heappop(max_heap)
            heaviest2=max_heap[0]
            if heaviest1==heaviest2:
                heapq.heappop(max_heap)
            else:
                res= heaviest1 - heaviest2
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, res)
        return -1*max_heap[0] if len(max_heap)==1 else 0