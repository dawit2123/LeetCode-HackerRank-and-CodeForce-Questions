class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        def is_palindrome(s, i, j):
            while i<=j:
                if s[j]!=s[i]:
                    return False
                i, j= i+1, j-1
            return True 
        dfs(0)
        return res                   