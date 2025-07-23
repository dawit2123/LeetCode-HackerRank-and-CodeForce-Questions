# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        inverted_piles= [-val for val in piles]
        heapq.heapify(inverted_piles)
        for _ in range(k):
            value= -1*heapq.heappop(inverted_piles)
            result= value- (value//2) if value-(value//2)>=0 else 0
            heapq.heappush(inverted_piles, -1*result)
        return -1*sum(inverted_piles)