class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L=0
        R=len(needle)
        while R<= len(haystack):
            if haystack[L:R]==needle:
                return L
            L+=1
            R+=1
        return -1