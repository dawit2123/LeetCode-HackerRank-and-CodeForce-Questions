class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={")":"(", "}":"{", "]":"["}
        stack=[]
        for c in s:
            if stack and c in hash_map and stack[-1]==hash_map[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack)==0