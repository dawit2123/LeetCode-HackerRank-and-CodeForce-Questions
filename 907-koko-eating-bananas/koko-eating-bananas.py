class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high= 1, max(piles)
        min_rate=high
        while low<=high:
            mid= (low+high)//2
            total_time=0
            for pile in piles:
                total_time+=math.ceil(pile/mid)
            if total_time<=h:
                high=mid-1
                min_rate=mid
            else:
                low=mid+1
        return min_rate