# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        output=0
        s_left=0
        g_left=0
        while g_left < len(g) and s_left < len(s) :
            if s[s_left]>=g[g_left]:
                output+=1
                g_left+=1
            s_left+=1
        return output
