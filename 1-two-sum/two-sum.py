class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map={}
        for i, n in enumerate(nums):
            complement_value= target-n
            if complement_value in prev_map:
                return [prev_map[complement_value], i]
            else:
                prev_map[n]=i
        return []