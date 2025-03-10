# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      L=0
      for R in range(1,len(nums)):
        if nums[R]==nums[L]:
            continue
        else:
            L+=1
            nums[L]=nums[R]
      return L+1