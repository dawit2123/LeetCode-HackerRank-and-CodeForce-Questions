# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq= Counter(nums)
        result=[]
        for key in freq.keys():
            if freq[key]>1:
                result.append(key)
        return result