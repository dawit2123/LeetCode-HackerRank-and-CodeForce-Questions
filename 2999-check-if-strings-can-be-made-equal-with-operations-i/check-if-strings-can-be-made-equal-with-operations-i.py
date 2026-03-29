class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_even_chars_sorted = sorted(s1[::2])
        s2_even_chars_sorted = sorted(s2[::2])
      
        # Extract and sort characters at odd positions (1, 3, 5, ...) from both strings
        s1_odd_chars_sorted = sorted(s1[1::2])
        s2_odd_chars_sorted = sorted(s2[1::2])
      
        # Both even and odd position characters must match after sorting
        return (s1_even_chars_sorted == s2_even_chars_sorted and 
                s1_odd_chars_sorted == s2_odd_chars_sorted)
