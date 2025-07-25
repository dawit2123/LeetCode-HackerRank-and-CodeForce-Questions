class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        nums.sort()
        visited=set()
        if nums[-1]<0:
            return nums[-1]
        else:
            temp_sum=0
            for i in range(len(nums)-1, -1, -1):
                if nums[i] not in visited:
                    temp_sum+=nums[i]
                    if temp_sum>0:
                        max_sum= max(max_sum, temp_sum)
                        visited.add(nums[i])
                    else:
                        temp_sum=0
        return max_sum if max_sum!=float('-inf') else 0