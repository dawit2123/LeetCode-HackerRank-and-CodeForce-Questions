# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        res = 0

        while queue:
            queue.pop() 
            res += queue.pop() 
            queue.popleft() 
        return res