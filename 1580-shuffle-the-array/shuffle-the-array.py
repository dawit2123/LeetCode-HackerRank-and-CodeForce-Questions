class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # iterate over the value from 0, n and build the combination of x and y
        for i in range(n):
            x=nums[i]<<10
            y=nums[i+n]
            nums[i]=x|y
        j=2*n-1
        for k in range(n-1, -1, -1):
            # extract the value of x and y
            x=nums[k]>>10
            y=nums[k]&((2**10)-1)
            nums[j]=y
            nums[j-1]=x
            j-=2
        return nums