class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        remain=total%p
        if remain==0:
            return 0
        remain_to_prefix={
            0:-1
        }
        res=len(nums)
        cur_sum=0
        for i, n in enumerate(nums):
            cur_sum=(cur_sum+n)%p
            prefix=(cur_sum-remain+p)%p
            if prefix in remain_to_prefix:
                length=i-remain_to_prefix[prefix]
                res=min(res, length)
            remain_to_prefix[cur_sum]=i
        return -1 if res==len(nums) else res