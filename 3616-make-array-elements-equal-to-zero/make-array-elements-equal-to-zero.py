class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Calculate the total sum of all elements in the array
        total_sum = sum(nums)
      
        # Initialize the count of valid selections and left sum
        valid_count = 0
        left_sum = 0
      
        # Iterate through each element in the array
        for num in nums:
            if num != 0:
                # If current element is non-zero, add it to the left sum
                left_sum += num
            else:
                # At a zero position, check if it's a valid selection point
              
                # If left sum equals right sum (perfectly balanced)
                # Both directions are valid, so add 2
                if left_sum * 2 == total_sum:
                    valid_count += 2
                  
                # If left and right sums differ by exactly 1
                # One direction is valid, so add 1
                elif abs(left_sum * 2 - total_sum) == 1:
                    valid_count += 1
      
        return valid_count