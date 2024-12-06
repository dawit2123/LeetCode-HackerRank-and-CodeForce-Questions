import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            total_hours=0
            for p in piles:
                total_hours+=(math.ceil(p/mid))
            if total_hours<=h:
                res=min(res, mid)
                r=mid-1
            else:
                l=mid+1
        return res