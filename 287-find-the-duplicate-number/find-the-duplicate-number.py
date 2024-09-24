class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers=defaultdict(int)
        for num in nums:
            if numbers[num]>0:
                return num
            numbers[num]+=1
        return -1
