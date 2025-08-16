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
