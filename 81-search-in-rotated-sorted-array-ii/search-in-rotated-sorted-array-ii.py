class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right= 0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[left]<nums[mid]:
                if target<nums[mid] and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[left]>nums[mid]:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                left+=1
        return False