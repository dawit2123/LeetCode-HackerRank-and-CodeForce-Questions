class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            val=nums[i]
            target=-val
            left, right=i+1, len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    result.append([val, nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return result