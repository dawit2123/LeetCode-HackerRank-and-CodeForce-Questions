class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=Counter(nums).keys()
        result=[]
        for key in nums:
            result.append(key)
        result.sort()
        if len(result)<3:
            return result[-1]
        return result[-3]