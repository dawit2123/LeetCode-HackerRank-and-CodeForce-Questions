class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequency=0
        nums_freq=Counter(nums)
        max_frequency= max(nums_freq.values())
        result=0
        for key in nums_freq.keys():
            if nums_freq[key]==max_frequency:
                result+=(nums_freq[key])
        return result