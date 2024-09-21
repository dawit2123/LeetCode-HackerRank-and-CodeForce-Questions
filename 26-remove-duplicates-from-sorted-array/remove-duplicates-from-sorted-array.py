class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      L=0
      k=0
      for R in range(1,len(nums)):
        if nums[R]==nums[L]:
            continue
        else:
            L+=1
            nums[L]=nums[R]
      k=max(k,L+1)
      return k