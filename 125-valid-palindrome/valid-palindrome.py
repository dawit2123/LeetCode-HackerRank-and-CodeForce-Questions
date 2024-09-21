class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while L<R:
            if not(s[R].isalnum()):
                R-=1
            elif not(s[L].isalnum()):
                L+=1
            else:
                if s[R].lower()!=s[L].lower():
                    return False
                R-=1
                L+=1
        return True
            