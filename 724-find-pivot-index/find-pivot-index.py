class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums=[]
        prefix=0
        print
        for num in nums:
            prefix+=num
            sum_nums.append(prefix)
        print(sum_nums)
        for i in range(len(sum_nums)):
            left=sum_nums[i-1] if i>0 else 0
            right=sum_nums[len(sum_nums)-1]-sum_nums[i] if i<len(sum_nums)-1 else 0
            if left==right:
                return i
        return -1