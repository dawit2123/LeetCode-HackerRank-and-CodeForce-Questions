# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        N = len(stones)
        total = sum(stones)
        target = total // 2

        @cache
        def most(i: int, r: int) -> int:
            """Returns the largest subset sum of stones[i:] that adds up to at most r (remaining knapsack capacity)"""

            if i == N or r == 0: return 0

            best = most(i+1, r)

            if stones[i] <= r:
                best = max(best, stones[i] + most(i+1, r-stones[i]))

            return best

        T = most(0, target)
        S = total - T
        return S - T