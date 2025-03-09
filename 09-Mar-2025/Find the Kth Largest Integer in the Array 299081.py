# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap=[int(num) for num in nums]
        heapq.heapify(min_heap)
        while k<len(min_heap):
            heapq.heappop(min_heap)
        return str(min_heap[0])