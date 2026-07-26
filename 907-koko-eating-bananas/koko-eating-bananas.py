import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high= 1, max(piles)
        min_rate=high
        if len(piles)==h:
            return high
        while low<=high:
            mid= (low+high)//2
            total_hours=0
            for pile in piles:
                total_hours+=(math.ceil((pile)/mid))
            if total_hours<=h:
                min_rate=mid
                high=mid-1
            else:
                low=mid+1
        return min_rate