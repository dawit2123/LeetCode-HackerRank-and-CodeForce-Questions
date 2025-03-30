class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_freq= Counter(nums)
        result=[0,0]
        for key in nums_freq:
            result[0]+=(nums_freq[key]//2)
            result[1]+=(nums_freq[key]%2)
        return result