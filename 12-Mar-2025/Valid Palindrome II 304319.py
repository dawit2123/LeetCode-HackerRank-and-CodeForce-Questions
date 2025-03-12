# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        L, R= 0, len(s)-1
        while L<R:
            if s[L]==s[R]:
                L+=1
                R-=1
            else:
               return helper(L, R-1) or helper(L+1, R)
        return True