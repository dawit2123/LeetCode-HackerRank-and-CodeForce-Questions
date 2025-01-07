class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimum_variation=float("inf")
        for i in range(len(nums)-k+1):
            variation= nums[i+k-1]- nums[i]
            minimum_variation= min(minimum_variation, variation)
        return minimum_variation