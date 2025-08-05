# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        next_coin = 1
        for coin in coins:
            if next_coin - coin < 0: 
                break
            next_coin += coin
        return next_coin