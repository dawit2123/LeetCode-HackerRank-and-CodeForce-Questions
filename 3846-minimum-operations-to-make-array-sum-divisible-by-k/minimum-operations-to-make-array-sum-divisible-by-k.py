class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_sum=sum(nums)
        return nums_sum-((nums_sum//k)*k)