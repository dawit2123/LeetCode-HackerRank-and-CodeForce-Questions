class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # initialize min_sum, target_index, count
        count=0
        while len(nums)>1:
            min_sum=float('inf')
            target_index=-1
            is_ascending=True
            # iterate over the values
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    is_ascending=False
                pair_sum= nums[i]+nums[i+1]
                if pair_sum<min_sum:
                    target_index=i
                    min_sum=pair_sum
            if is_ascending:
                break
            count+=1
            nums[target_index]=min_sum
            nums.pop(target_index+1)
        return count