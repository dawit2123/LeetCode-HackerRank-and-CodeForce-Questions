class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for num in nums:
            count[num]+=1
        print(count)
        i=0
        for j, n in enumerate(count):
            for _ in range(n):
                nums[i]=j
                i+=1
        return nums
        