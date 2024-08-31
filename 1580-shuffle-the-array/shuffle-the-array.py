class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        numbers=[]
        for i in range(0,n):
            numbers.append(nums[i])
            numbers.append(nums[i+n])
        return numbers
