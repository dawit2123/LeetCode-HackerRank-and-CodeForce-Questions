class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap={")":"(","]":"[","}":"{"}
        stack=[]
        for i in s:
            if(i in "({["):
                stack.append(i);
            else:
                if stack and stack[-1]==hashmap[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
               