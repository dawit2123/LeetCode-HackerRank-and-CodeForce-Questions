# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(buyFlag,i):
            if i >= len(prices):
                return 0
            if buyFlag:
                return max(rec(False,i+2) + prices[i],rec(True,i+1))
            else:
                return max(rec(True,i+1)-prices[i],rec(False,i+1))

        return rec(False,0)        
