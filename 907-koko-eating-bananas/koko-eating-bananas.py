class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high= 1, max(piles)
        min_rate=high
        while low<=high:
            mid=(low+high)//2
            sum_hours=0
            for pile in piles:
                sum_hours+=int(math.ceil(pile/mid))
            if sum_hours>h:
                low=mid+1
            else:
                high=mid-1
                min_rate=mid
        return min_rate