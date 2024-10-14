class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score=0
        numbers=[-num for num in nums]
        heapq.heapify(numbers)
        while k>0:
            val=-(heapq.heappop(numbers))
            score+=val
            heapq.heappush(numbers, -math.ceil(val/3))
            k-=1
        return score