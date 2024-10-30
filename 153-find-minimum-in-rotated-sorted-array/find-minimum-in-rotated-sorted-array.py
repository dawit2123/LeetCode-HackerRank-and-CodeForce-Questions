class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        return nums[0]