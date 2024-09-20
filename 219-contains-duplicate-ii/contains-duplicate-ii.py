class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_visited={}
        for i in range(len(nums)):
            if nums[i] in hash_visited and abs(i- hash_visited[nums[i]])<=k:
                return True
            hash_visited[nums[i]]=i
        return False
            