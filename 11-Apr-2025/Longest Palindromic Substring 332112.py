# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=[0, 0]
        for i in range(len(s)):
            res= self.helper(s, i, i)
            if (res[1]-res[0])> (longest[1]- longest[0]):
                longest[1]= res[1]
                longest[0]= res[0]

            res= self.helper(s, i, i+1)
            if (res[1]-res[0])> (longest[1]- longest[0]):
                longest[1]= res[1]
                longest[0]= res[0]
        return s[longest[0]:longest[1]+1]
            
    def helper(self,s, l, r):
        max_longest=[0,0]
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l) > (max_longest[1]-max_longest[0]):
                max_longest[1]=r
                max_longest[0]=l
            l-=1
            r+=1
        return max_longest