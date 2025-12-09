class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left_counter = Counter()  # Tracks frequency of elements seen so far (left side)
        right_counter = Counter(nums)  # Initially contains all elements (right side)
      
        result = 0
        MOD = 10**9 + 7
      
        for current_num in nums:
            right_counter[current_num] -= 1
            double_value = current_num * 2
            triplet_count = (left_counter[double_value] * right_counter[double_value]) % MOD
            result = (result + triplet_count) % MOD
          
            left_counter[current_num] += 1
      
        return result