import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        max_heap=[]
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, (-1*num, i))
            if i>=k-1:
                while max_heap[0][1]<=i-k:
                    heapq.heappop(max_heap)
                result.append(-1*max_heap[0][0])
        return result