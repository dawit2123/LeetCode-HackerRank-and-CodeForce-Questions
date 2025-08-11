# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)      
        dp[0] = 1
        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]
        return dp[-1]
