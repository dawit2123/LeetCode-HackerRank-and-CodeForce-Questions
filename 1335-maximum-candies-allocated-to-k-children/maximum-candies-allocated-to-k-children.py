from typing import List  

class Solution:  
    def maximumCandies(self, candies: List[int], k: int) -> int:  
        # Initialize the search range for the maximum candies per child  
        left, right = 1, max(candies)  
        result = 0  # This will hold the maximum number of candies that can be distributed to each child  

        # Perform binary search to find the maximum candies that can be distributed  
        while left <= right:  
            mid = (left + right) // 2  # Calculate the mid-point of the current search range  

            # Count how many children can be satisfied with mid candies  
            children_count = sum(pile // mid for pile in candies)  

            # If we can satisfy at least k children, it is a valid distribution  
            if children_count >= k:  
                result = mid  # Update result to the current mid, as it's a potential answer  
                left = mid + 1  # Try for more candies  
            else:  
                # If we can't satisfy k children, reduce the amount of candies being distributed  
                right = mid - 1  
                
        return result  # Return the maximum number of candies that can be equally distributed  