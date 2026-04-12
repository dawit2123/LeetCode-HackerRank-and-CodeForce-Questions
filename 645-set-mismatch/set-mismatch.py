from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_freq=Counter(nums)
        duplicated, missed= 0, 0
        for i in range(1, len(nums)+1):
            if i not in nums_freq:
                missed=i
            elif nums_freq[i]==2:
                duplicated=i
        return [duplicated, missed]