class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_list=Counter(nums)
        for key in nums_list:
            if nums_list[key]%2!=0:
                return False
        return True