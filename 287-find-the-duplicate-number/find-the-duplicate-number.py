class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=nums[0]
        while True:
            if slow==slow2:
                return slow
            slow=nums[slow]
            slow2=nums[slow2]
