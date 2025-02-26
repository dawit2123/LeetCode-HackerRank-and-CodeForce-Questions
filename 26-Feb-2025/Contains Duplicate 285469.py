# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets= set()
        for num in nums:
            if num in sets:
                return True
            else:
                sets.add(num)
        return False