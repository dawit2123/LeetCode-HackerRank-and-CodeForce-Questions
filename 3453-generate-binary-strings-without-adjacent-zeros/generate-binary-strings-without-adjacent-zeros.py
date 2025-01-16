class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def helper(substring):
            if len(substring)==n:
                res.append(substring)
                return
            helper(substring+"1")
            if substring[-1]=="1":
                helper(substring+"0")
        helper("0")
        helper("1")
        return res