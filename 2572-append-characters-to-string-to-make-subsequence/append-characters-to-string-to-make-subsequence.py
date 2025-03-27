class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_length = len(t)
        for c in s:
            if t_length and c == t[-t_length]:
                t_length -= 1
        return t_length