class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(open, close, cur):
            if  open>n or close>n:
                return 
            if open==close==n:
                res.append(cur)
            dfs(open+1, close, cur+"(")
            if open!=close: dfs(open, close+1, cur+")")
        dfs(1,0, "(")
        return res         