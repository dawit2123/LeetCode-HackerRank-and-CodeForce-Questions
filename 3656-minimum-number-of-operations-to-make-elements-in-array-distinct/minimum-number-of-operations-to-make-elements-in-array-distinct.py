class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        required_nums=0
        hash_map=Counter(nums)
        i=0
        while max(hash_map.values())>1 and i<len(nums):
            required_nums+=1
            max_boundary=i+3
            while i<len(nums) and i<max_boundary:
                hash_map[nums[i]]-=1
                i+=1
        return required_nums
            