class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n, h = len(prices), k >> 1
        base = prev = nxt = best = 0

        for i in range(n):
            base += strategy[i] * prices[i]

        for i in range(k):
            prev += strategy[i] * prices[i]
            if i >= h:
                nxt += prices[i]

        best = max(0, nxt - prev)

        for r in range(k, n):
            l = r - k + 1
            prev += strategy[r] * prices[r] - strategy[l - 1] * prices[l - 1]
            nxt += prices[r] - prices[l - 1 + h]
            best = max(best, nxt - prev)

        return base + best