class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen,res,cur=set(),[],''   
        for ch in s:
            cur+=ch
            if cur in seen: continue
            seen.add(cur); res.append(cur); cur=''
        return res