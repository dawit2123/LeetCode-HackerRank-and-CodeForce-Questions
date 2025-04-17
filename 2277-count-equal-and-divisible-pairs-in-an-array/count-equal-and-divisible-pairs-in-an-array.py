class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        number_of_pairs=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    number_of_pairs+=1
        return number_of_pairs