class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq= Counter(nums)
        result=[]
        for key in freq.keys():
            if freq[key]>1:
                result.append(key)
        return result