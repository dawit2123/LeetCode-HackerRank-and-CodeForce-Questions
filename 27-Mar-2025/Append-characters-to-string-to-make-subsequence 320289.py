# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_length = len(t)
        for c in s:
            if t_length and c == t[-t_length]:
                t_length -= 1
        return t_length