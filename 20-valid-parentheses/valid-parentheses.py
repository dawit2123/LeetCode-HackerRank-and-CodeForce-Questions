class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={")":"(", "}":"{", "]":"["}
        stack=[]
        for c in s:
            if stack and c in hash_map:
                if stack and hash_map[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0