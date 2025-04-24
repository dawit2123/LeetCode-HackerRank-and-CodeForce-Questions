# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
      hash_map={"}":"{", ")":"(", "]":"["}
      stack=[s[0]]
      for i in range(1, len(s)):
        if s[i] in hash_map and stack[-1]==hash_map[s[i]]:
            stack.pop()
        else:
            stack.append(s[i])
      return len(stack)==0  