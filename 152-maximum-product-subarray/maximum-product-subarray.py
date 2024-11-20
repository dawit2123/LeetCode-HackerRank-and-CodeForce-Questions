class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cur_max, cur_min=1,1
        for n in nums:
            if n==0:
                cur_max, cur_min=1,1
                continue
            temp=n*cur_max
            cur_max=max(temp, n*cur_min, n)
            cur_min=min(temp, n*cur_min, n)
            res=max(cur_max, res)
            print(res)
        return res