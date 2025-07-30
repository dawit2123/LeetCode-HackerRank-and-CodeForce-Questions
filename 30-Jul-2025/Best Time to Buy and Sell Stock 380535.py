# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=0
        min_buy=prices[0]
        for sell in prices:
            if sell-min_buy>0:
                max_p=max(max_p, sell-min_buy)
            min_buy=min(min_buy, sell)
        return max_p