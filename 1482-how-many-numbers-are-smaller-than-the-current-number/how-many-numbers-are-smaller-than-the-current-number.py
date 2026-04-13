from bisect import bisect_left
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted= sorted(nums)
        return [bisect_left(nums_sorted, num) for num in nums]