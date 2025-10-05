class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_set=set()
        left=0
        max_window_size=0
        for right in range(len(s)):
            while s[right] in window_set:
                window_set.remove(s[left])
                left+=1
            window_set.add(s[right])
            max_window_size=max(max_window_size, right-left+1)
        return max_window_size