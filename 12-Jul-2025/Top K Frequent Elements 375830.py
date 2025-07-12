# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_obj=defaultdict(int)
        for num in nums:
            nums_obj[num]+=1
        sorted_by_occurence_nums= sorted(nums_obj.keys(), key=lambda key: nums_obj[key], reverse=True)
        return sorted_by_occurence_nums[0:k]
        