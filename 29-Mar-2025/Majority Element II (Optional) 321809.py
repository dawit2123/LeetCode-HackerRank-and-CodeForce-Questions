# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements_count=Counter(nums)
        res=[]
        threshold= len(nums)//3
        for element , count in elements_count.items():
            if count > threshold:
                res.append(element)
        return res
