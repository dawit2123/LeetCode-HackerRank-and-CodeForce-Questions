class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer=[]
        n=len(nums)
        for num in nums:
            num= abs(num)
            if nums[num-1]<0:
                answer.append(num)
            nums[num-1]*=-1
        return answer