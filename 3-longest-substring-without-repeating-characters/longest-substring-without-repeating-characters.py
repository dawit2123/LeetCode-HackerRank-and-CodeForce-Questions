class Solution:
    def lengthOfLongestSubstring(self ,s: str) -> int:
        # Dictionary to store the last index of each character
        last_index = {}

        # Left pointer of sliding window
        left = 0

        # Variable to track maximum window length found
        max_len = 0

        # Iterate through string using right pointer
        for right, char in enumerate(s):

            # If char already seen AND its last index is inside current window
            if char in last_index and last_index[char] >= left:
                # Move left pointer to one position after previous occurrence
                left = last_index[char] + 1

            # Update the last seen index of current character
            last_index[char] = right

            # Update longest window length
            max_len = max(max_len, right - left + 1)

        # Return the maximum substring length
        return max_len
