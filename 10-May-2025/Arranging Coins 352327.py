# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        res=0
        while l<=r:
            mid=(l+r)//2
            temp=(mid*(mid+1))/2
            if temp<=n:
                res=max(res, mid)
                l=mid+1
            else:
                r=mid-1
        return res
