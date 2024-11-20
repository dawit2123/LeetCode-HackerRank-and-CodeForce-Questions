class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        l=0
        count_p= Counter(p)
        for r in range(len(p), len(s)+1):
            if Counter(s[l:r])==count_p:
                res.append(l)
            l+=1
        return res