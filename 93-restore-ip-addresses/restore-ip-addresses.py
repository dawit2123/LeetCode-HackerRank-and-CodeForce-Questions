class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return res
        def helper(i, dot, cur_ip):
            if i==len(s) and dot==4:
                res.append(cur_ip[:-1])
                return
            if dot>4:
                return
            
            for j in range(i, min(i+3, len(s))):
                
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    print(s[i], i, j)
                    helper(j+1, dot+1, cur_ip+s[i:j+1]+".")
        helper(0,0,"")
        return res