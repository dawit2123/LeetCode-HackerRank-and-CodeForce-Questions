class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=2
        nums_count=Counter(nums)
        temp=float('-inf')
        res=0
        for num in nums_count:
            if nums_count[num]>=n//2 and nums_count[num]>temp:
                temp=nums_count[num]
                res=num
        return res