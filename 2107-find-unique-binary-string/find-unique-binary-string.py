class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set= {s for s in nums}
        def helper(i, current_nums):
            if i==len(nums):
                current_str="".join(current_nums)
                return None if current_str in nums_set else current_str
            res= helper(i+1, current_nums)
            if res: return res
            current_nums[i]="1"
            res= helper(i+1, current_nums)
            if res: return res
        return helper(0, ["0" for num in nums])