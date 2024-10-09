class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in range(0,len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif (stack[-1]+s[i])=="()":
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)