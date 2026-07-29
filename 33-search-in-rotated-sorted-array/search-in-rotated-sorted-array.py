class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right-=1
                else:
                    left+=1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left+=1
                else:
                    right-=1
        return -1