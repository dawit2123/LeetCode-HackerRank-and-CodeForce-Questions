class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(opened, closed, cur):
            if opened==closed==n:
                res.append(cur)
                return
            if opened<n:
                dfs(opened+1, closed, cur+"(")
            if closed<opened:
                dfs(opened, closed+1, cur+")")
        dfs(0, 0, "")
        return res
                